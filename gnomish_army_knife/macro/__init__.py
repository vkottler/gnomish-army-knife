"""
A module implementing macro interfaces.
"""

# built-in
from os import linesep

# third-party
from vcorelib.dict.codec import BasicDictCodec as _BasicDictCodec
from vcorelib.io.types import JsonObject as _JsonObject

# internal
from gnomish_army_knife.icon import icon_url
from gnomish_army_knife.schemas import GakDictCodec


class Macro(GakDictCodec, _BasicDictCodec):
    """A class implementing an interface for macros."""

    short_markdown: str

    def init(self, data: _JsonObject) -> None:
        """Perform implementation-specific initialization."""

        super().init(data)

        # Icon and label.
        # h1 - class page (or 'generic').
        # h2 - spec / category
        lines: list[str] = [
            f"### {icon_url(str(data['icon']))} {data['label']}"
        ]

        # Macro description.
        if data.get("markdown"):
            lines.append(data["markdown"])  # type: ignore
            del data["markdown"]

        # Macro title and text.
        lines.append(f"Title: `{data['title']}`.")
        lines.append(
            linesep.join(
                ["```", data["text"], "```"],  # type: ignore
            )
        )

        self.short_markdown = (linesep + linesep).join(lines)

        self.set_markdown(markdown=self.short_markdown, config=data)
