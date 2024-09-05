"""
A module implementing a simple event log server task.
"""

# built-in
import argparse
import asyncio
from queue import Queue
from threading import Event, Thread
from time import sleep

# third-party
from runtimepy.net.arbiter import AppInfo
from runtimepy.net.arbiter.task import ArbiterTask
from runtimepy.primitives import Uint32

# internal
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.net.connection import CombatLogEventConnection
from gnomish_army_knife.runtime import GakRuntime


class LogServerTask(ArbiterTask):
    """A class implementing a runtime environment for an event log server."""

    queue: Queue[CombatLogEvent]

    runtime: GakRuntime

    stop_reading_log: Event
    log_file_reader_thread: Thread

    # Metrics.
    event_count: Uint32

    # No stateful elements are currently allocated during (runtime) init.
    auto_finalize = True

    def _init_state(self) -> None:
        """Add channels to this instance's channel environment."""

        self.event_count = Uint32()
        self.env.channel("event_count", self.event_count)

    def log_file_reader_main(self) -> None:
        """
        A thread entry for processing the latest/active combat log and
        servicing any queue or handler consumers.
        """

        self.logger.info("Combat-log reading thread started.")

        while not self.stop_reading_log.is_set():
            # Ensure we don't starve due to no active log file.
            sleep(0.1)

            latest = self.runtime.latest_combat_log()
            if latest is not None:
                self.runtime.database.logs.process_log(
                    latest, stop=self.stop_reading_log
                )

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)

        self.queue = Queue()
        self.stop_reading_log = Event()

        # Parse command-line options and create the runtime instance.
        parser = argparse.ArgumentParser()
        GakRuntime.cli_args(parser)
        self.runtime = app.stack.enter_context(
            GakRuntime.create(
                parser.parse_args(
                    app.config.get(  # type: ignore
                        "gak_cli_args",
                        [],
                    )
                )
            )
        )

        # Connect queue to event stream.
        app.stack.enter_context(
            self.runtime.database.logs.queue.registered(self.queue)
        )

        # Create and start log-file-reading thread.
        self.log_file_reader_thread = Thread(target=self.log_file_reader_main)
        self.log_file_reader_thread.start()

    async def stop_extra(self) -> None:
        """Extra actions to perform when this task is stopping."""

        # Signal log-reading thread to stop and wait for it to be stopped.
        self.stop_reading_log.set()
        self.log_file_reader_thread.join()
        self.logger.info("Combat-log reading thread stopped.")

    async def dispatch(self) -> bool:
        """Dispatch an iteration of this task."""

        while not self.queue.empty():
            item = self.queue.get_nowait()
            self.event_count.increment()
            for conn in self.app.search(kind=CombatLogEventConnection):
                conn.forward_handler(item)

            # Ensure other things get to run if the queue is populated at or
            # greater than the rate of forwarding.
            await asyncio.sleep(0)

        return True
