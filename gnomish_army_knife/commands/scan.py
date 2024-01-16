"""
An entry-point for the 'scan' command.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace

# third-party
from vcorelib.args import CommandFunction as _CommandFunction

# internal
from gnomish_army_knife.runtime import GakRuntime


def scan_cmd(args: _Namespace) -> int:
    """Execute the scan command."""

    with GakRuntime.create(args) as runtime:
        runtime.logger.info("Scan command.")

    return 0


def add_scan_cmd(parser: _ArgumentParser) -> _CommandFunction:
    """Add arbiter-command arguments to its parser."""

    GakRuntime.cli_args(parser)

    return scan_cmd
