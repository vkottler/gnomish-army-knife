"""
A module implementing a macro database structure.
"""

# built-in
from pathlib import Path

# third-party
from vcorelib.io.types import JsonObject as _JsonObject
from vcorelib.paths.find import find_file

# internal
from gnomish_army_knife import PKG_SLUG
from gnomish_army_knife.macro.category import MacroCategory
from gnomish_army_knife.schemas import BasicGakCodec

DEFAULT_MACRO_DATABASE = f"package://{PKG_SLUG}/macros.yaml"


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

    def write_markdown(self, path: Path) -> None:
        """Write markdown contents to disk."""

        assert self.categories, "No macro categories loaded!"

        path.mkdir(parents=True, exist_ok=True)

        # index page, include self's markdown (from init) + link to categories

        # create category pages (implement in category class)
