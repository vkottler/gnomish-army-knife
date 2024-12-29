"""
Test the 'macro.database' module.
"""

# built-in
from pathlib import Path

# module under test
from gnomish_army_knife.macro.category import MacroCategory
from gnomish_army_knife.macro.database import DEFAULT_OUT, MacroDatabase
from gnomish_army_knife.macro.group import MacroGroup


def test_macro_database_rendering():
    """Test rendering a macro database to markdown."""

    MacroDatabase.load().write_markdown_dir(Path(DEFAULT_OUT))


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
