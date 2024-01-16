"""
An entry-point for the 'scan' command.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from pathlib import Path

# third-party
from vcorelib.args import CommandFunction as _CommandFunction

# internal
from gnomish_army_knife import DEFAULT_CONFIG
from gnomish_army_knife.config import get_config
from gnomish_army_knife.paths import wow_dir


def scan_cmd(args: _Namespace) -> int:
    """Execute the scan command."""

    config = get_config(args)

    print(wow_dir(args, config))

    return 0


def add_scan_cmd(parser: _ArgumentParser) -> _CommandFunction:
    """Add arbiter-command arguments to its parser."""

    parser.add_argument(
        "-c",
        "--config",
        default=DEFAULT_CONFIG,
        type=Path,
        help="path to an optional configuration file",
    )

    return scan_cmd
