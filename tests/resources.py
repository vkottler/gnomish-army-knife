"""
A module for working with test data.
"""

# built-in
from pathlib import Path


def resource(resource_name: str, *parts: str, valid: bool = True) -> Path:
    """Locate the path to a test resource."""

    return Path(__file__).parent.joinpath(
        "data", "valid" if valid else "invalid", resource_name, *parts
    )


def wow_test_dir() -> Path:
    """Get the test WoW directory."""

    return resource("World of Warcraft")


def sample_event_log() -> Path:
    """Get a sample event log."""

    return wow_test_dir().joinpath(
        "_retail_", "Logs", "WoWCombatLog-030225_222539.txt"
    )
