"""
A module implementing an interface for macro groups.
"""

# built-in
from os import linesep
from pathlib import Path

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
        self.slug: str = self.to_slug(self.name)

        self.macros: list[Macro] = [
            # Schema has already been validated.
            Macro(x, verify=False)  # type: ignore
            for x in data.get(  # type: ignore
                "macros",
                [],
            )
        ]

    def write_markdown(
        self, parent_name: str, parent_icon_url: str, path: Path
    ) -> None:
        """Write markdown contents to disk."""

        with path.open("w") as path_fd:
            path_fd.write(
                linesep.join(
                    [
                        f"# {self.icon_url} {self.name}",
                        "",
                        f"([{parent_icon_url}](index.html) "
                        f"[{parent_name}](index.html))",
                        "",
                        "## Macros",
                        "",
                        "TODO",
                        "",
                    ]
                    + list(self.markdown_footer)
                )
            )
