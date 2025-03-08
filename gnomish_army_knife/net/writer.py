"""
A module implementing an arena-match database writer task.
"""

# built-in
from queue import Queue

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
