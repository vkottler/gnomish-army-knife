"""
A module implementing a combat-log state data structure.
"""

# third-party
from vcorelib.dict.codec import BasicDictCodec as _BasicDictCodec

# internal
from gnomish_army_knife.schemas import GakDictCodec


class CombatLogState(GakDictCodec, _BasicDictCodec):
    """The top-level configuration object for the package."""
