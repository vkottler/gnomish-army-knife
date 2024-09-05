"""
A module implementing a network-connection interfaces.
"""

# built-in
from datetime import datetime

# third-party
from runtimepy.message import JsonMessage
from runtimepy.net.stream.json import JsonMessageConnection

# internal
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.database.queue import CombatLogQueueHandler


class CombatLogEventConnection(JsonMessageConnection):
    """
    A class implementing a connection interface for exchanging combat-log
    events.
    """

    # Connect handlers to this queue to receive incoming events.
    queue: CombatLogQueueHandler

    def forward_handler(self, event: CombatLogEvent) -> None:
        """Handle a combat log event."""
        self.send_json({"event": event.as_json()})

    async def event_handler(
        self, response: JsonMessage, data: JsonMessage
    ) -> None:
        """Service this connection's queue."""

        del response
        self.queue.handle(
            CombatLogEvent(
                datetime.fromisoformat(data["timestamp"]),
                data["name"],
                data["data"],
            )
        )

    def init(self) -> None:
        """Initialize this instance."""

        super().init()
        self.queue = CombatLogQueueHandler()

    def _register_handlers(self) -> None:
        """Register connection-specific command handlers."""

        super()._register_handlers()
        self.basic_handler("event", self.event_handler)
