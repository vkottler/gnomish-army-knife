"""
A module implementing an arena-match metadata interface.
"""

# built-in
from pathlib import Path
from typing import Optional

# internal
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.enums.events import LogEvent


class ArenaMatchMetadata:
    """A class implementing an arena-match metadata interface."""

    def __init__(self) -> None:
        """Initialize this instance."""

        # sub-directory for map (instanceID), get filename from timestamp
        # build mapping of unit ID to player name and get player names, too?

        self.reset()

    @property
    def summary(self) -> str:
        """A summary string for this match."""

        return ""

    def _match_start(self, event: CombatLogEvent) -> None:
        """Handle the match start event."""

        # MATCH_START: instanceID, unk, matchType, teamId
        # MATCH_START,1505,0,Skirmish,0

        # atinylittleshell/wow-combat-log-parser/src/actions/ArenaMatchStart.ts

        del event

    def _match_end(self, event: CombatLogEvent) -> None:
        """Handle the match end event."""

        # MATCH_END: winningTeam, duration, newRatingTeam1, newRatingTeam2
        # MATCH_END,0,58,0,0

        del event

    def _combatant_info(self, event: CombatLogEvent) -> None:
        """Handle the combatant info event."""

        del event

    def handle(self, event: CombatLogEvent) -> None:
        """Attempt to glean new metadata from this event."""

        match event.name:
            case LogEvent.MATCH_START:
                self._match_start(event)
            case LogEvent.MATCH_END:
                self._match_end(event)
            case LogEvent.COMBATANT_INFO:
                self._combatant_info(event)

    def reset(self) -> None:
        """Reset metadata state."""

    def file_path(self) -> Optional[Path]:
        """
        Get a file path this match could be written to. This path should be
        unique for any match that occurs on live servers.
        """

        result = None

        return result
