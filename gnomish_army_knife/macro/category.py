"""
A module implementing an interface for macro categories.
"""

# third-party
from vcorelib.io.types import JsonObject as _JsonObject

# internal
from gnomish_army_knife.icon import icon_url
from gnomish_army_knife.macro import Macro
from gnomish_army_knife.macro.group import MacroGroup
from gnomish_army_knife.schemas import BasicGakCodec


class MacroCategory(BasicGakCodec):
    """A class implementing an interface for macros."""

    def init(self, data: _JsonObject) -> None:
        """Perform implementation-specific initialization."""

        super().init(data)

        self.groups: list[MacroGroup] = [
            # Schema has already been validated.
            MacroGroup(x, verify=False)  # type: ignore
            for x in data.get(  # type: ignore
                "groups",
                [],
            )
        ]

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
