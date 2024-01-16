"""
A module implementing interfaces for working with file-system paths related
to a World of Warcraft installation.
"""

# built-in
from argparse import Namespace as _Namespace
from pathlib import Path

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
