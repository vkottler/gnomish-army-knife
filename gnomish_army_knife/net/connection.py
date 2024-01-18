"""
A module implementing a network-connection interfaces.
"""

# third-party
from runtimepy.net.stream.json import JsonMessageConnection

# internal
from gnomish_army_knife.database.event import CombatLogEvent


class CombatLogEventConnection(JsonMessageConnection):
    """
    A class implementing a connection interface for exchanging combat-log
    events.
    """

    # need to implement a message handler for the events? should we make a
    # schema for it?

    def forward_handler(self, event: CombatLogEvent) -> None:
        """Handle a combat log event."""
        self.send_json(event.as_json())
