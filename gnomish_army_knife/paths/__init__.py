"""
A module implementing interfaces for working with file-system paths related
to a World of Warcraft installation.
"""

# built-in
from argparse import Namespace as _Namespace
from datetime import datetime
from pathlib import Path
from typing import Union

# internal
from gnomish_army_knife import WOW_DIR
from gnomish_army_knife.config import Config


def wow_dir(args: _Namespace, config: Config) -> Path:
    """A method for locating the 'World of Warcraft' directory."""

    search_paths: list[Path] = [args.config.parent, Path()] + [
        Path(x) for x in config.data.get("search_paths", [])  # type: ignore
    ]

    found = False

    for path in search_paths:
        result = path.joinpath(WOW_DIR)
        if result.is_dir():
            found = True
            break

    assert found, f"Couldn't find '{WOW_DIR}' in: {search_paths}."

    return result


COMBAT_LOG_PREFIX = "WoWCombatLog-"


def combat_log_slug(path: Path) -> str:
    """Get the non-boilerplate parts of a combat log file name."""
    return path.with_suffix("").name.replace(COMBAT_LOG_PREFIX, "")


def combat_log_datetime(slug: Union[Path, str]) -> datetime:
    """Get a datetime instance based on the log slug."""

    if isinstance(slug, Path):
        slug = combat_log_slug(slug)
    return datetime.strptime(slug, "%m%d%y_%H%M%S")


def path_is_combat_log(path: Path) -> bool:
    """Determine if a given path points to a combat log file."""
    return path.name.startswith(COMBAT_LOG_PREFIX)
