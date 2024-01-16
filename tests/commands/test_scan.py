"""
Test the 'commands.scan' module.
"""

# built-in
from contextlib import ExitStack
from tempfile import TemporaryDirectory

# third-party
from vcorelib.paths.context import in_dir

# module under test
from gnomish_army_knife import DEFAULT_CONFIG, PKG_NAME
from gnomish_army_knife.entry import main as gnomish_army_knife_main

# internal
from tests.resources import resource


def test_entry_basic():
    """Test basic scan invocations."""

    base = [PKG_NAME, "scan"]

    with ExitStack() as stack:
        stack.enter_context(in_dir(resource(DEFAULT_CONFIG).parent))

        args = ["--state", stack.enter_context(TemporaryDirectory())]

        assert gnomish_army_knife_main(base + args) == 0
