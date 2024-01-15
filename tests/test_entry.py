"""
gnomish_army_knife - Test the program's entry-point.
"""

# built-in
from subprocess import check_output
from sys import executable
from unittest.mock import patch

# module under test
from gnomish_army_knife import PKG_NAME
from gnomish_army_knife.entry import main as gnomish_army_knife_main


def test_entry_basic():
    """Test basic argument parsing."""

    args = [PKG_NAME, "noop"]
    assert gnomish_army_knife_main(args) == 0

    with patch("gnomish_army_knife.entry.entry", side_effect=SystemExit(1)):
        assert gnomish_army_knife_main(args) != 0


def test_package_entry():
    """Test the command-line entry through the 'python -m' invocation."""

    check_output([executable, "-m", "gnomish_army_knife", "-h"])
