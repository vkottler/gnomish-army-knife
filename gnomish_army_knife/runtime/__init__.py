"""
A module implementing this package's runtime environment.
"""

# built-in
from argparse import ArgumentParser as _ArgumentParser
from argparse import Namespace as _Namespace
from pathlib import Path

# third-party
from runtimepy.mixins.environment import ChannelEnvironmentMixin
from vcorelib.logging import LoggerMixin

# internal
from gnomish_army_knife import DEFAULT_CONFIG
from gnomish_army_knife.config import get_config
from gnomish_army_knife.paths import wow_dir


class GakRuntime(ChannelEnvironmentMixin, LoggerMixin):
    """A class implementing a runtime environment interface."""

    def __init__(self, args: _Namespace) -> None:
        """Initialize this instance."""

        ChannelEnvironmentMixin.__init__(self)
        LoggerMixin.__init__(self)

        self.config = get_config(args)
        self.wow_dir = wow_dir(args, self.config)
        self.logger.info(
            "Using '%s' as installation directory.", self.wow_dir.resolve()
        )

    @staticmethod
    def cli_args(parser: _ArgumentParser) -> None:
        """Add command-line argumments related to the runtime environment."""

        parser.add_argument(
            "-c",
            "--config",
            default=DEFAULT_CONFIG,
            type=Path,
            help="path to an optional configuration file",
        )
