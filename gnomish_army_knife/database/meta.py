"""
A module implementing an arena-match metadata interface.
"""

# built-in
from pathlib import Path
from typing import Optional

# third-party
from vcorelib.logging import LoggerMixin

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

        # sub-directory for map (instanceID), get filename from timestamp
        # build mapping of unit ID to player name and get player names, too?

        self.seen_match_start: bool = False
        self.seen_match_end: bool = False
        self.combatant_info_count: int = 0

        self.instance: str = ""

        self.reset()

    @property
    def summary(self) -> str:
        """A summary string for this match."""

        return f"({self.instance})"

    def _match_start(self, event: CombatLogEvent) -> None:
        """Handle the match start event."""

        inst_id = int(event.data[0])
        self.instance = ARENAS.get(inst_id, event.data[0])

        self.logger.info(
            "Instance: %s, (%d?).", self.instance, int(event.data[1])
        )

        # MATCH_START: instanceID, unk, matchType, teamId
        # MATCH_START,1505,0,Skirmish,0

        # atinylittleshell/wow-combat-log-parser/src/actions/ArenaMatchStart.ts

        self.seen_match_start = True

    def _match_end(self, event: CombatLogEvent) -> None:
        """Handle the match end event."""

        # MATCH_END: winningTeam, duration, newRatingTeam1, newRatingTeam2
        # MATCH_END,0,58,0,0

        # self.logger.info(event.data)

        del event

        self.seen_match_end = True

    def _combatant_info(self, event: CombatLogEvent) -> None:
        """Handle the combatant info event."""

        del event

    def handle(self, event: CombatLogEvent) -> bool:
        """
        Attempt to glean new metadata from this event. Returns whether or not
        the end of a match has been captured.
        """

        result = False

        match event.name:
            case LogEvent.MATCH_START:
                self.reset()
                self._match_start(event)
                self.seen_match_start = True

            case LogEvent.COMBATANT_INFO:
                if self.seen_match_start:
                    self._combatant_info(event)
                    self.combatant_info_count += 1

            case LogEvent.MATCH_END:
                if self.seen_match_start:
                    self._match_end(event)
                    self.seen_match_end = True
                    result = True

        return result

    def reset(self) -> None:
        """Reset metadata state."""

        self.seen_match_start = False
        self.seen_match_end = False
        self.combatant_info_count = 0
        self.instance = ""

    def file_path(self) -> Optional[Path]:
        """
        Get a file path this match could be written to. This path should be
        unique for any match that occurs on live servers.
        """

        # https://docs.python.org/3/library/uuid.html#uuid.uuid4
        # need to use this and use JSON cache file thing to keep metadata
        # databases to determine the attributes of the match stored in the file
        # with the generated uuid

        result = None

        # do we need combatant info for anything?
        if self.seen_match_start and self.seen_match_end:
            pass

        return result
