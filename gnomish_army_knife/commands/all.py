# =====================================
# generator=datazen
# version=3.2.0
# hash=4331c5cb512c29fba9fa6d90509366a2
# =====================================

"""
A module aggregating package commands.
"""

# built-in
from typing import List as _List
from typing import Tuple as _Tuple

# third-party
from vcorelib.args import CommandRegister as _CommandRegister

# internal
from gnomish_army_knife.commands.markdown import add_markdown_cmd
from gnomish_army_knife.commands.scan import add_scan_cmd


def commands() -> _List[_Tuple[str, str, _CommandRegister]]:
    """Get this package's commands."""

    return [
        (
            "markdown",
            "generate Markdown content from class data",
            add_markdown_cmd,
        ),
        (
            "scan",
            "scan the 'World of Warcraft' directory for updates",
            add_scan_cmd,
        ),
        ("noop", "command stub (does nothing)", lambda _: lambda _: 0),
    ]
