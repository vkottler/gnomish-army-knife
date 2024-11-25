"""
Test the 'commands.markdown' module.
"""

# built-in
from contextlib import ExitStack
from tempfile import TemporaryDirectory

# third-party
from vcorelib.paths.context import in_dir

# module under test
from gnomish_army_knife import PKG_NAME
from gnomish_army_knife.entry import main as gnomish_army_knife_main


def test_markdown_basic():
    """Test basic markdown invocations."""

    base = [PKG_NAME, "markdown"]

    with ExitStack() as stack:
        # Generate in a temporary directory.
        stack.enter_context(in_dir(stack.enter_context(TemporaryDirectory())))

        assert gnomish_army_knife_main(base) == 0
