"""
A module implementing a configuration interface for the package.
"""

# third-party
from vcorelib.dict.codec import BasicDictCodec as _BasicDictCodec

# internal
from gnomish_army_knife.schemas import GakDictCodec


class Config(GakDictCodec, _BasicDictCodec):
    """The top-level configuration object for the package."""
