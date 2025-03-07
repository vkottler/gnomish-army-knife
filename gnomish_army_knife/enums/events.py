"""
A module implementing an enumeration for important combat log events.
"""

# bulit-in
from enum import StrEnum


class LogEvent(StrEnum):
    """An enumeration for combat log event names."""

    MATCH_START = "ARENA_MATCH_START"
    MATCH_END = "ARENA_MATCH_END"
    COMBATANT_INFO = "COMBATANT_INFO"
