"""
A module implementing a user interface task that consumes combat event
messages.
"""

# built-in
from queue import Queue

# third-party
from runtimepy.net.arbiter import AppInfo
from runtimepy.net.arbiter.task import TaskFactory

# internal
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.net.connection import CombatLogEventConnection
from gnomish_army_knife.runtime.task import GakRuntimeTask


class UiTask(GakRuntimeTask):
    """A class that manages user-interface interactions."""

    queues: dict[CombatLogEventConnection, tuple[Queue[CombatLogEvent], int]]

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)
        self.queues = {}

    async def dispatch(self) -> bool:
        """Dispatch an iteration of this task."""

        # log some info when connection state changed

        # essentially copied from LogWriterTask
        inactive = set()
        active = set()
        for conn in self.app.conn_manager.by_type(CombatLogEventConnection):
            active.add(conn)
            if conn not in self.queues:
                queue: Queue[CombatLogEvent] = Queue()
                self.queues[conn] = (queue, conn.queue.register(queue))
        for conn in self.queues:
            if conn not in active:
                inactive.add(conn)
        for conn in inactive:
            conn.queue.remove(self.queues[conn][1])
            del self.queues[conn]

        # get events
        for queue, _ in self.queues.values():
            if not queue.empty():
                # play sound?

                while not queue.empty():
                    pass

                # play sound?

        return True


class GakUi(TaskFactory[UiTask]):
    """A class implementing a log-writer task factory."""

    kind = UiTask
