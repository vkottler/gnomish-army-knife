"""
A module implementing a macro database structure.
"""

# built-in
from os import linesep
from pathlib import Path

# third-party
from vcorelib.io.types import JsonObject as _JsonObject
from vcorelib.paths.find import find_file

# internal
from gnomish_army_knife import PKG_NAME, PKG_SLUG
from gnomish_army_knife.macro.category import MacroCategory
from gnomish_army_knife.schemas import BasicGakCodec

DEFAULT_MACRO_DATABASE = f"package://{PKG_SLUG}/macros.yaml"
DEFAULT_OUT = f"{PKG_NAME}-markdown"


class MacroDatabase(BasicGakCodec):
    """A class implementing an interface for macros."""

    @staticmethod
    def load(path: Path | str = DEFAULT_MACRO_DATABASE) -> "MacroDatabase":
        """Load a macro database from disk."""

        return MacroDatabase.decode(
            find_file(path, include_cwd=True, strict=True)
        )

    def init(self, data: _JsonObject) -> None:
        """Perform implementation-specific initialization."""

        super().init(data)

        self.categories: list[MacroCategory] = [
            # Schema has already been validated.
            MacroCategory(x, verify=False)  # type: ignore
            for x in data.get(  # type: ignore
                "categories",
                [],
            )
        ]
        self.title: str = data["title"]  # type: ignore

    def write_markdown_dir(self, path: Path, name: str = "index.md") -> None:
        """Write markdown contents to disk."""

        assert self.categories, "No macro categories loaded!"

        path.mkdir(parents=True, exist_ok=True)

        link_strs: list[str] = []
        for category in self.categories:
            link = f"{category.slug}/index.html"
            link_strs.append(
                f"## [{category.icon_url}]({link}) [{category.name}]({link})"
            )

            if category.groups:
                link_strs.append("")

            # Direct links to groups.
            for group in category.groups:
                link = f"{category.slug}/{group.slug}.html"
                link_strs.append(
                    f" * [{group.icon_url}]({link}) [{group.name}]({link})"
                )

            category.write_markdown_dir(
                path.joinpath(category.slug), name=name
            )

        link_strs.append("")

        # Index.
        with path.joinpath(name).open("w") as path_fd:
            path_fd.write(
                linesep.join(
                    [f"# {self.title}", ""]
                    + link_strs
                    + list(self.markdown_footer)
                )
            )
