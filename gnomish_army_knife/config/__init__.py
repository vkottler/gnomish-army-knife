"""
A module implementing a configuration interface for the package.
"""

# built-in
from argparse import Namespace as _Namespace

# third-party
from vcorelib.dict.codec import BasicDictCodec as _BasicDictCodec

# internal
from gnomish_army_knife.schemas import GakDictCodec


class Config(GakDictCodec, _BasicDictCodec):
    """The top-level configuration object for the package."""


def get_config(args: _Namespace) -> Config:
    """Get a configuration instance based on parsed command-line arguments."""

    return (
        Config.decode(args.config)
        if args.config.is_file()
        else Config.create({})
    )
