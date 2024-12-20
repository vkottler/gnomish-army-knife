"""
An entry-point for the 'markdown' command.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from pathlib import Path

# third-party
from vcorelib.args import CommandFunction as _CommandFunction

# internal
from gnomish_army_knife.macro.database import (
    DEFAULT_MACRO_DATABASE,
    DEFAULT_OUT,
    MacroDatabase,
)


def markdown_cmd(args: _Namespace) -> int:
    """Execute the markdown command."""

    MacroDatabase.load(args.database).write_markdown_dir(args.output)

    return 0


def add_markdown_cmd(parser: _ArgumentParser) -> _CommandFunction:
    """Add markdown-command arguments to its parser."""

    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="output directory (default: '%(default)s')",
        default=DEFAULT_OUT,
    )

    parser.add_argument(
        "-d",
        "--database",
        help="macro database (default: '%(default)s')",
        default=DEFAULT_MACRO_DATABASE,
    )

    return markdown_cmd
