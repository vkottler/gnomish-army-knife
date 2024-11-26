"""
Test the 'macro' module.
"""

# module under test
from gnomish_army_knife.macro import Macro


def test_macro_basic():
    """Test basic interactions with macro instances."""

    macro = Macro.create({"markdown": "# what up"})
    assert macro.markdown
