"""
Test the 'macro.database' module.
"""

# module under test
from gnomish_army_knife.macro.database import (
    MacroCategory,
    MacroDatabase,
    MacroGroup,
)


def test_macro_database_basic():
    """Test basic interactions with macro database instances."""

    for kind, data in [
        (MacroDatabase, {"markdown": "MacroDatabase description."}),
        (
            MacroGroup,
            {"name": "class name", "markdown": "MacroGroup description."},
        ),
        (
            MacroCategory,
            {"name": "spec name", "markdown": "MacroCategory description."},
        ),
    ]:
        inst = kind.create(data)  # type: ignore
        assert inst.markdown
        # print(inst.markdown)

    # assert False
