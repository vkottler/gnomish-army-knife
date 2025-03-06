"""
A module implementing an arena-match metadata interface.
"""

# built-in
from pathlib import Path
from typing import Optional

# internal
from gnomish_army_knife.database.event import CombatLogEvent


class ArenaMatchMetadata:
    """A class implementing an arena-match metadata interface."""

    def __init__(self) -> None:
        """Initialize this instance."""

        # sub-directory for map (instanceID), get filename from timestamp
        # build mapping of unit ID to player name and get player names, too?

        # MATCH_START: instanceID, unk, matchType, teamId
        # MATCH_START,1505,0,Skirmish,0

        # MATCH_END: winningTeam, duration, newRatingTeam1, newRatingTeam2
        # MATCH_END,0,58,0,0

        # atinylittleshell/wow-combat-log-parser/src/actions/ArenaMatchStart.ts

        self.reset()

    @property
    def summary(self) -> str:
        """A summary string for this match."""

        return ""

    def handle(self, event: CombatLogEvent) -> None:
        """Attempt to glean new metadata from this event."""

    def reset(self) -> None:
        """Reset metadata state."""

    def file_path(self) -> Optional[Path]:
        """TODO."""

        result = None

        return result
