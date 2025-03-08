"""
A module implementing interfaces for combat log events.
"""

# built-in
from datetime import datetime
from time import strptime
from typing import Callable, NamedTuple

# third-party
from runtimepy.message import JsonMessage
from vcorelib.logging import LoggerType

# internal
from gnomish_army_knife.enums.events import LogEvent

CombatLogEventHandler = Callable[["CombatLogEvent"], None]


def parse_timestamp(data: str) -> datetime:
    """Parse a timestamp string from a combat log line."""

    # Parse the timestamp.
    datetime_raw, millis = data.split(".")

    # Ignore timezone suffix (non-standard).
    millis = millis.split("-")[0].split("+")[0]

    timestamp = datetime(
        *strptime(datetime_raw, "%m/%d/%Y %H:%M:%S")[:6],
        microsecond=int(millis) * 1000,
    )

    return timestamp


class CombatLogEvent(NamedTuple):
    """A simple container for combat log events."""

    timestamp: datetime
    name: str
    data: list[str]
    line: str

    def as_json(self) -> JsonMessage:
        """Create a JSON serializable dictionary from this instance."""

        return {
            "timestamp": str(self.timestamp),
            "name": self.name,
            # This complex data structure is not parsed correctly for some
            # events.
            "data": (
                self.data if not self.name == LogEvent.COMBATANT_INFO else []
            ),
            "line": self.line,
        }

    @staticmethod
    def from_json(data: JsonMessage) -> "CombatLogEvent":
        """Create an event from JSON message data."""

        return CombatLogEvent(
            datetime.fromisoformat(data["timestamp"]),
            data["name"],
            data["data"],
            data["line"],
        )

    @staticmethod
    def from_line(line: str) -> "CombatLogEvent":
        """Create an event from a string line."""

        timestamp_raw, event_raw = line.rstrip().split("  ", 1)
        event_items = event_raw.split(",")

        return CombatLogEvent(
            parse_timestamp(timestamp_raw),
            event_items[0],
            event_items[1:],
            line,
        )

    def log(self, logger: LoggerType) -> None:
        """Log this event."""
        logger.info("(%s) %s: %s.", self.timestamp, self.name, self.data)

    @staticmethod
    def log_handler(logger: LoggerType) -> CombatLogEventHandler:
        """Create a simple event handler."""

        def handler(event: CombatLogEvent) -> None:
            """A simple event handler that logs."""
            event.log(logger)

        return handler
