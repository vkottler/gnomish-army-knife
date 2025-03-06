"""
A module implementing a simple event log server task.
"""

# built-in
import asyncio
from queue import Queue
from threading import Event, Thread
from time import sleep

# third-party
from runtimepy.net.arbiter import AppInfo

# internal
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.database.writer import ArenaMatchWriter
from gnomish_army_knife.net.connection import CombatLogEventConnection
from gnomish_army_knife.runtime.task import GakRuntimeTask


class LogWriterTask(GakRuntimeTask):
    """A class that writes incoming arena match data to a file database."""

    writers: dict[
        CombatLogEventConnection,
        tuple[ArenaMatchWriter, Queue[CombatLogEvent], int],
    ]

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)
        self.writers = {}

    async def dispatch(self) -> bool:
        """Dispatch an iteration of this task."""

        inactive = set()

        # Determine which connections are still active or need writing
        # interfaces.
        active = set()
        for conn in self.app.conn_manager.by_type(CombatLogEventConnection):
            active.add(conn)

            # should move this to some kind of "connection instance created"
            # callback (need runtimepy to support this), maybe just "connected"
            # callback? (that can fire multiple times i.e. on re-connect?)
            # should be a connect/disconnect callback thing?
            if conn not in self.writers:
                writer = self.runtime.database.create_writer()
                queue: Queue[CombatLogEvent] = Queue()
                self.writers[conn] = (
                    writer,
                    queue,
                    conn.queue.register(queue),
                )

        # Clean up inactive writers (could move this to disconnect callback
        # system described above).
        for conn in self.writers:
            if conn not in active:
                inactive.add(conn)
        for conn in inactive:
            conn.queue.remove(self.writers[conn][2])
            del self.writers[conn]

        # Handle connection events.
        for conn, (writer, queue, _) in self.writers.items():
            while not queue.empty():
                event = queue.get_nowait()

                # Could count ignored events at some point.
                if await writer.handle(event):
                    self.event_count.increment()

        return True


class LogServerTask(GakRuntimeTask):
    """A class implementing a runtime environment for an event log server."""

    queue: Queue[CombatLogEvent]
    stop_reading_log: Event
    log_file_reader_thread: Thread

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

            # Forward events to connected clients.
            for conn in self.app.conn_manager.by_type(
                CombatLogEventConnection
            ):
                conn.forward_handler(item)

            # Ensure other things get to run if the queue is populated at or
            # greater than the rate of forwarding.
            await asyncio.sleep(0)

        return True
