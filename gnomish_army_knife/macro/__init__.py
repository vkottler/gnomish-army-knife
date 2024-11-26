"""
A module implementing macro interfaces.
"""

# third-party
from vcorelib.dict.codec import BasicDictCodec as _BasicDictCodec
from vcorelib.io.types import JsonObject as _JsonObject

# internal
from gnomish_army_knife.schemas import GakDictCodec


class Macro(GakDictCodec, _BasicDictCodec):
    """A class implementing an interface for macros."""

    def init(self, data: _JsonObject) -> None:
        """Perform implementation-specific initialization."""

        super().init(data)
        self.set_markdown(config=data)
