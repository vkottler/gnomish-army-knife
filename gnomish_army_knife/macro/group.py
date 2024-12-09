"""
A module implementing an interface for macro groups.
"""

# third-party
from vcorelib.io.types import JsonObject as _JsonObject

# internal
from gnomish_army_knife.icon import icon_url
from gnomish_army_knife.macro import Macro
from gnomish_army_knife.schemas import BasicGakCodec


class MacroGroup(BasicGakCodec):
    """A class implementing an interface for macros."""

    def init(self, data: _JsonObject) -> None:
        """Perform implementation-specific initialization."""

        super().init(data)

        self.icon_url = icon_url(str(data["icon"]))
        self.name: str = data["name"]  # type: ignore

        self.macros: list[Macro] = [
            # Schema has already been validated.
            Macro(x, verify=False)  # type: ignore
            for x in data.get(  # type: ignore
                "macros",
                [],
            )
        ]
