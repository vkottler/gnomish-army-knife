"""
A module implementing an interface for macro categories.
"""

# built-in
from os import linesep
from pathlib import Path

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
        self.slug: str = self.to_slug(self.name)

        self.macros: list[Macro] = [
            # Schema has already been validated.
            Macro(x, verify=False)  # type: ignore
            for x in data.get(  # type: ignore
                "macros",
                [],
            )
        ]

    def write_markdown_dir(self, path: Path, name: str = "index.md") -> None:
        """Write markdown contents to disk."""

        path.mkdir(parents=True, exist_ok=True)

        # Group pages.
        link_strs: list[str] = []
        for group in self.groups:
            group.write_markdown(
                self.name, self.icon_url, path.joinpath(f"{group.slug}.md")
            )
            link = f"{group.slug}.html"
            link_strs.append(
                f"* [{group.icon_url}]({link}) [{group.name}]({link})"
            )

        link_strs.append("")

        with path.joinpath(name).open("w") as path_fd:
            path_fd.write(
                linesep.join(
                    [
                        f"# {self.icon_url} {self.name}",
                        "",
                        "([top-level](..))",
                        "",
                        "## Groups",
                        "",
                    ]
                    + link_strs
                    + ["", "## Macros", "", "TODO", ""]
                    + list(self.markdown_footer),
                )
            )
