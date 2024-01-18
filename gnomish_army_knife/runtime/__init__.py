"""
A module implementing this package's runtime environment.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from contextlib import ExitStack, contextmanager
from pathlib import Path
from typing import Iterator

from rcmpy.xdg import user_state

# third-party
from runtimepy.mixins.environment import ChannelEnvironmentMixin
from vcorelib.logging import LoggerMixin

# internal
from gnomish_army_knife import DEFAULT_CONFIG, PKG_ABBREV
from gnomish_army_knife.config import get_config
from gnomish_army_knife.database import ArenaMatchDb
from gnomish_army_knife.paths import path_is_combat_log, wow_dir


class GakRuntime(ChannelEnvironmentMixin, LoggerMixin):
    """A class implementing a runtime environment interface."""

    def __init__(self, stack: ExitStack, args: _Namespace) -> None:
        """Initialize this instance."""

        ChannelEnvironmentMixin.__init__(self)
        LoggerMixin.__init__(self)

        self.config = get_config(args)

        self.wow_dir = wow_dir(args, self.config)
        self.logger.info(
            "Using '%s' as installation directory.", self.wow_dir.resolve()
        )

        self.database = ArenaMatchDb(stack, args.state)

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

    @staticmethod
    @contextmanager
    def create(args: _Namespace) -> Iterator["GakRuntime"]:
        """Create a runtime instance as a context."""

        with ExitStack() as stack:
            yield GakRuntime(stack, args)
