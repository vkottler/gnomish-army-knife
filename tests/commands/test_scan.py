"""
Test the 'commands.scan' module.
"""

# third-party
from vcorelib.paths.context import in_dir

# module under test
from gnomish_army_knife import DEFAULT_CONFIG, PKG_NAME
from gnomish_army_knife.entry import main as gnomish_army_knife_main

# internal
from tests.resources import resource


def test_entry_basic():
    """Test basic scan invocations."""

    with in_dir(resource(DEFAULT_CONFIG).parent):
        args = [PKG_NAME, "scan"]
        assert gnomish_army_knife_main(args) == 0
