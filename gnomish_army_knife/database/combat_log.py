"""
A module implementing a combat-log state data structure.
"""

# built-in
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from time import strptime
from typing import Any

# third-party
from vcorelib import DEFAULT_ENCODING
from vcorelib.dict.codec import BasicDictCodec as _BasicDictCodec
from vcorelib.io import JsonObject as _JsonObject
from vcorelib.logging import LoggerMixin

# internal
from gnomish_army_knife.database.event import (
    CombatLogEvent,
    CombatLogEventHandler,
)
from gnomish_army_knife.paths import combat_log_datetime, combat_log_slug
from gnomish_army_knife.schemas import GakDictCodec

VERSION_EVENT = "COMBAT_LOG_VERSION"


class CombatLogState(GakDictCodec, _BasicDictCodec, LoggerMixin):
    """The top-level configuration object for the package."""

    def init(self, data: _JsonObject) -> None:
        """Initialize this instance."""

        self.data = data

        self.data.setdefault("files", {})

        LoggerMixin.__init__(self)

        self.handlers: dict[str, CombatLogEventHandler] = {}
        self.missing_handlers: dict[str, set[str]] = defaultdict(set)

    @property
    def files(self) -> dict[str, Any]:
        """Get combat log file data."""
        return self.data["files"]  # type: ignore

    def process_event(self, key: str, event: CombatLogEvent) -> None:
        """Process a combat-log event."""

        file_data: dict[str, Any] = self.data["files"][key]  # type: ignore

        if event.name in self.handlers:
            self.handlers[event.name](event)
        elif event.name not in self.missing_handlers[key]:
            self.missing_handlers[key].add(event.name)
            file_data["missing_handlers"].append(event.name)

        file_data["event_totals"][event.name] += 1

    def process_line(self, key: str, line: str, log_date: datetime) -> None:
        """Process a line from a combat log file."""

        timestamp_raw, event_raw = line.split("  ", 1)

        # Parse the timestamp.
        datetime_raw, millis = timestamp_raw.split(".")
        timestamp = datetime(
            log_date.year,
            *strptime(datetime_raw, "%m/%d %H:%M:%S")[1:6],
            microsecond=int(millis) * 1000,
        )

        # Parse the event data.
        event_items = event_raw.split(",")
        self.process_event(
            key, CombatLogEvent(timestamp, event_items[0], event_items[1:])
        )

    def process_log(self, path: Path) -> None:
        """Process a combat log file."""

        key = combat_log_slug(path)
        file_data = self.files.setdefault(key, {"state": "processing"})

        # Return early if this log has already been processed.
        if file_data["state"] == "reached_eof":
            return

        file_data.setdefault("position", 0)

        # Log some information about this file.
        date = combat_log_datetime(key)

        file_data["datetime"] = str(date)
        file_data["timestamp"] = date.timestamp()
        file_data["event_totals"] = defaultdict(int)
        file_data["missing_handlers"] = []

        self.logger.info(
            "Processing log '%s' (%s old) from position %d.",
            date,
            datetime.now() - date,
            file_data["position"],
        )

        with path.open(encoding=DEFAULT_ENCODING) as log:
            # Go back to a possible previous iteration's starting point.
            log.seek(file_data["position"])

            reached_eof = False
            while not reached_eof:
                line = log.readline().rstrip()
                if line:
                    # This is some kind of bug in the client? Event lines with
                    # no timestamp, and only for this event.
                    if line.startswith(VERSION_EVENT):
                        parsed = line.split(",")
                        self.process_event(
                            key, CombatLogEvent(date, parsed[0], parsed[1:])
                        )
                    else:
                        self.process_line(key, line, date)
                else:
                    file_data["state"] = "reached_eof"
                    reached_eof = True

                # Always update position after a line is processed.
                file_data["position"] = log.tell()

        self.logger.info(
            "Reached EOF for log '%s' (%d event types weren't handled).",
            date,
            len(file_data["missing_handlers"]),
        )
        self.logger.debug(file_data)
