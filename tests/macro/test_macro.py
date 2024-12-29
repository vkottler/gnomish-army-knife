"""
Test the 'macro' module.
"""

# built-in
from os import linesep

# module under test
from gnomish_army_knife.macro import Macro


def test_macro_basic():
    """Test basic interactions with macro instances."""

    macro = Macro.create(
        {
            "label": "Example Macro",
            "text": linesep.join(["#showtooltip", "", "/cast spell"]),
            "markdown": "Macro description.",
        }
    )

    # print(macro.short_markdown)
    # print(macro.markdown)
    # assert False

    assert macro.markdown
