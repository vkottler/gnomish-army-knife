"""
A module implementing a macro database structure.
"""

# third-party
from vcorelib.dict.codec import BasicDictCodec as _BasicDictCodec
from vcorelib.io.types import JsonObject as _JsonObject

# internal
from gnomish_army_knife.schemas import GakDictCodec


class BasicGakCodec(GakDictCodec, _BasicDictCodec):
    """A base class for schema-backed objects."""

    def init(self, data: _JsonObject) -> None:
        """Perform implementation-specific initialization."""

        super().init(data)
        self.set_markdown(config=data)


class MacroDatabase(BasicGakCodec):
    """A class implementing an interface for macros."""

    # add interfaces to write index markdown + top-level-category specific


class MacroGroup(BasicGakCodec):
    """A class implementing an interface for macros."""


class MacroCategory(BasicGakCodec):
    """A class implementing an interface for macros."""
