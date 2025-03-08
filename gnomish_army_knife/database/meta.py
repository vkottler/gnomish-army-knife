"""
A module implementing an arena-match metadata interface.
"""

# built-in
from pathlib import Path
from typing import Any, Optional, cast
import uuid

# third-party
from vcorelib.io.types import JsonObject
from vcorelib.logging import LoggerMixin
from vcorelib.math import to_nanos
from vcorelib.math.time import nano_str

# internal
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.enums.events import LogEvent

# https://wago.tools/db2/Map?filter%5BInstanceType%5D=4&page=1
ARENAS = {
    559: "Nagrand Arena (old)",
    562: "zzOldBlade's Edge Arena",
    572: "Ruins of Lordaeron",
    617: "Dalaran Sewers",
    618: "The Ring of Valor",
    980: "Tol'Viron Arena",
    1134: "The Tiger's Peak",
    1170: "Shado-Pan Showdown",
    1504: "Black Rook Hold Arena",
    1505: "Nagrand Arena",
    1552: "Ashamane's Fall",
    1672: "Blade's Edge Arena",
    1825: "Hook Point",
    1911: "Mugambala",
    2167: "The Robodrome",
    2373: "Empyrean Domain",
    2509: "Maldraxxus Coliseum",
    2511: "Enigma Arena",
    2547: "Enigma Crucible",
    2563: "Nokhudon Proving Grounds",
    2759: "Cage of Carnage",
}


class ArenaMatchMetadata(LoggerMixin):
    """A class implementing an arena-match metadata interface."""

    def __init__(self) -> None:
        """Initialize this instance."""

        super().__init__()

        self.seen_match_start: bool = False
        self.seen_match_end: bool = False
        self.data: JsonObject = {}
        self.reset()

    @property
    def summary(self) -> str:
        """A summary string for this match."""

        return (
            f"({'WIN' if self.data['is_win'] else 'LOSS'}"
            f" in {self.data['duration']}s) "
            f"{self.data['match_type']} on {self.data['instance']},"
            f" {self.data['unknown']}?"
        )

    def _match_start(self, event: CombatLogEvent) -> None:
        """Handle the match start event."""

        # MATCH_START: instanceID, unk, matchType, teamId
        # MATCH_START,1505,0,Skirmish,0
        # another example
        # atinylittleshell/wow-combat-log-parser/src/actions/ArenaMatchStart.ts

        # These should always be the same for i.e. solo shuffle rounds.
        if not self.seen_match_start:
            self.data["instance_id"] = int(event.data[0])
            self.data["instance"] = ARENAS.get(
                cast(int, self.data["instance_id"]), event.data[0]
            )
            self.data["unknown"] = event.data[1]
            self.data["match_type"] = event.data[2]
            self.data["team_id"] = int(event.data[3])

        self.seen_match_start = True

    def _match_end(self, event: CombatLogEvent) -> None:
        """Handle the match end event."""

        # MATCH_END: winningTeam, duration, newRatingTeam1, newRatingTeam2
        # MATCH_END,0,58,0,0

        self.data["winning_team_id"] = int(event.data[0])
        self.data["is_win"] = (
            self.data["team_id"] == self.data["winning_team_id"]
        )
        self.data["duration_s"] = int(event.data[1])
        self.data["duration"] = nano_str(
            to_nanos(cast(int, self.data["duration_s"])), is_time=True
        )
        self.data["new_rating_team_1"] = int(event.data[2])
        self.data["new_rating_team_2"] = int(event.data[3])

        self.data["summary"] = self.summary

        self.seen_match_end = True

    def handle(self, event: CombatLogEvent) -> bool:
        """
        Attempt to glean new metadata from this event. Returns whether or not
        the end of a match has been captured.
        """

        result = False

        events: dict[str, Any] = self.data["events"]  # type: ignore
        keep_metadata = False

        match event.name:
            case LogEvent.MATCH_START:
                self._match_start(event)
                keep_metadata = True

            case LogEvent.COMBATANT_INFO:
                # No special actions taken for this event currently.
                if self.seen_match_start:
                    keep_metadata = True

            case LogEvent.MATCH_END:
                if self.seen_match_start:
                    self._match_end(event)
                    result = True
                    keep_metadata = True

        if keep_metadata:
            if event.name in events:
                if not isinstance(events[event.name], list):
                    events[event.name] = [events[event.name]]
                events[event.name].append(event.as_json())
            else:
                events[event.name] = event.as_json()

            self.data["metadata_event_count"] += 1  # type: ignore

        return result

    def reset(self) -> None:
        """Reset metadata state."""

        self.seen_match_start = False
        self.seen_match_end = False
        self.data = {"events": {}, "metadata_event_count": 0}

    def file_path(self, base: Path, suffix: str = ".txt") -> Optional[Path]:
        """
        Get a file path this match could be written to. This path should be
        unique for any match that occurs on live servers.
        """

        result = None

        if self.seen_match_start and self.seen_match_end:
            result = Path(
                cast(str, self.data["match_type"]),
                cast(str, self.data["instance"]),
            )

            name = f"{uuid.uuid4()}{suffix}"
            while result.joinpath(name).is_file():  # pragma: nocover
                name = f"{uuid.uuid4()}{suffix}"

            result = base.joinpath(result, name)

        return result
