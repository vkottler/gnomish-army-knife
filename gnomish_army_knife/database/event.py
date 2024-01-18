"""
A module implementing interfaces for combat log events.
"""

# built-in
from datetime import datetime
from typing import Callable, NamedTuple

# third-party
from vcorelib.logging import LoggerType

CombatLogEventHandler = Callable[["CombatLogEvent"], None]


class CombatLogEvent(NamedTuple):
    """A simple container for combat log events."""

    timestamp: datetime
    name: str
    data: list[str]

    @staticmethod
    def log_handler(logger: LoggerType) -> CombatLogEventHandler:
        """Create a simple event handler."""

        def handler(event: CombatLogEvent) -> None:
            """A simple event handler that logs."""

            logger.info(
                "(%s) %s: %s.", event.timestamp, event.name, event.data
            )

        return handler
