"""
Test the 'macro.database' module.
"""

# module under test
from gnomish_army_knife.macro.category import MacroCategory
from gnomish_army_knife.macro.database import MacroDatabase
from gnomish_army_knife.macro.group import MacroGroup


def dev_dump(data: MacroDatabase) -> None:
    """Test method."""

    for category in data.categories:
        print(category.name)
        print(category.icon_url)

        for macro in category.macros:
            print(macro)

        for group in category.groups:
            print(group.name)
            print(group.icon_url)
            for macro in group.macros:
                print(macro)

    assert False


def test_macro_database_rendering():
    """Test rendering a macro database to markdown."""

    data = MacroDatabase.load()
    # dev_dump(data)
    del data


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
