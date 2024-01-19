"""
A module implementing this package's runtime environment.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from contextlib import ExitStack, contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Iterator, Optional

# third-party
from rcmpy.xdg import user_state
from runtimepy.mixins.environment import ChannelEnvironmentMixin
from vcorelib.logging import LoggerMixin

# internal
from gnomish_army_knife import DEFAULT_CONFIG, PKG_ABBREV
from gnomish_army_knife.config import Config
from gnomish_army_knife.database import ArenaMatchDb
from gnomish_army_knife.paths import (
    combat_log_datetime,
    path_is_combat_log,
    wow_dir,
)


class GakRuntime(ChannelEnvironmentMixin, LoggerMixin):
    """A class implementing a runtime environment interface."""

    def __init__(self, stack: ExitStack, args: _Namespace) -> None:
        """Initialize this instance."""

        ChannelEnvironmentMixin.__init__(self)
        LoggerMixin.__init__(self)

        self.config = Config.decode(args.config, require_success=False)

        self.wow_dir = wow_dir(args, self.config)
        self.logger.info(
            "Using '%s' as installation directory.", self.wow_dir.resolve()
        )

        state = (
            args.state
            if not args.ephemeral
            # pylint: disable=consider-using-with
            else Path(stack.enter_context(TemporaryDirectory()))
            # pylint: enable=consider-using-with
        )

        self.database = ArenaMatchDb(stack, state)

    @property
    def retail(self) -> Path:
        """Get the root path to the retail WoW installation."""
        return self.wow_dir.joinpath("_retail_")

    @property
    def combat_logs(self) -> Iterator[Path]:
        """Iterate over combat logs found."""

        base = self.retail.joinpath("Logs")
        for item in base.iterdir():
            if path_is_combat_log(item):
                yield item

    def latest_combat_log(self) -> Optional[Path]:
        """Attempt to get the most recent combat-log file."""

        latest = None

        logs = list(self.combat_logs)
        if logs:
            latest = logs[0]
            latest_time = combat_log_datetime(latest)
            for log in logs[1:]:
                curr_time = combat_log_datetime(log)
                if curr_time > latest_time:
                    latest = log
                    latest_time = curr_time

        return latest

    @staticmethod
    def cli_args(parser: _ArgumentParser) -> None:
        """Add command-line argumments related to the runtime environment."""

        parser.add_argument(
            "-c",
            "--config",
            default=DEFAULT_CONFIG,
            type=Path,
            help=(
                "path to an optional configuration file "
                "(default: '%(default)s')"
            ),
        )
        parser.add_argument(
            "-s",
            "--state",
            default=user_state(PKG_ABBREV),
            type=Path,
            help=(
                "path to the program's state directory "
                "(default: '%(default)s')"
            ),
        )
        parser.add_argument(
            "-e",
            "--ephemeral",
            action="store_true",
            help="set to use new, temporary directories when applicable",
        )

    @staticmethod
    @contextmanager
    def create(args: _Namespace) -> Iterator["GakRuntime"]:
        """Create a runtime instance as a context."""

        with ExitStack() as stack:
            yield GakRuntime(stack, args)
