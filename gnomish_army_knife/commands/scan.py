"""
An entry-point for the 'scan' command.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace

# third-party
from vcorelib.args import CommandFunction as _CommandFunction

# internal
from gnomish_army_knife.database.combat_log import VERSION_EVENT
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.runtime import GakRuntime


def scan_cmd(args: _Namespace) -> int:
    """Execute the scan command."""

    with GakRuntime.create(args) as runtime:
        # Add a simple handler.
        runtime.database.logs.handlers[VERSION_EVENT] = (
            CombatLogEvent.log_handler(runtime.database.logs.logger)
        )

        # Process combat logs.
        for log in runtime.combat_logs:
            with runtime.log_time("processing '%s'", log.name):
                runtime.database.logs.process_log(log)

    return 0


def add_scan_cmd(parser: _ArgumentParser) -> _CommandFunction:
    """Add arbiter-command arguments to its parser."""

    GakRuntime.cli_args(parser)

    return scan_cmd
