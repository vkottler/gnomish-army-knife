"""
A module implementing a network-connection interfaces.
"""

# third-party
from runtimepy.message import JsonMessage
from runtimepy.net.stream.json import JsonMessageConnection

# internal
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.database.queue import CombatLogQueueHandler
from gnomish_army_knife.enums.events import LogEvent


class CombatLogEventConnection(JsonMessageConnection):
    """
    A class implementing a connection interface for exchanging combat-log
    events.
    """

    # Connect handlers to this queue to receive incoming events.
    queue: CombatLogQueueHandler

    watch_names: set[str] = {LogEvent.MATCH_START, LogEvent.MATCH_END}

    def forward_handler(self, event: CombatLogEvent) -> None:
        """Handle a combat log event."""
        self.send_json({"event": event.as_json()})

    async def event_handler(
        self, response: JsonMessage, data: JsonMessage
    ) -> None:
        """Service this connection's queue."""

        del response

        event = CombatLogEvent.from_json(data)

        # Log watched events.
        if event.name in self.watch_names:
            event.log(self.logger)

        # Service queues.
        self.queue.handle(event)

    def init(self) -> None:
        """Initialize this instance."""

        super().init()
        self.queue = CombatLogQueueHandler()

    def _register_handlers(self) -> None:
        """Register connection-specific command handlers."""

        super()._register_handlers()
        self.basic_handler("event", self.event_handler)
