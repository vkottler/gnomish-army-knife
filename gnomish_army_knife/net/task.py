"""
A module implementing a simple event log server task.
"""

# built-in
import argparse
from queue import Queue

# third-party
from runtimepy.net.arbiter import AppInfo
from runtimepy.net.arbiter.task import ArbiterTask

# internal
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.net.connection import CombatLogEventConnection
from gnomish_army_knife.runtime import GakRuntime


class LogServerTask(ArbiterTask):
    """A class implementing a runtime environment for an event log server."""

    queue: Queue[CombatLogEvent]
    clients: list[CombatLogEventConnection]

    runtime: GakRuntime

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)

        self.queue = Queue()
        self.clients = list(app.search(kind=CombatLogEventConnection))

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

        # Add state for events processed counter?

        self.env.finalize()

    async def dispatch(self) -> bool:
        """Dispatch an iteration of this task."""

        while not self.queue.empty():
            item = self.queue.get_nowait()
            # count?
            for conn in self.clients:
                conn.forward_handler(item)

        return True
