# =====================================
# generator=datazen
# version=3.2.4
# hash=f4256143f73cfcee94dcf8635a09a9fe
# =====================================

"""
A module aggregating package commands.
"""

# third-party
from vcorelib.args import CommandRegister as _CommandRegister

# internal
from gnomish_army_knife.commands.markdown import add_markdown_cmd
from gnomish_army_knife.commands.scan import add_scan_cmd


def commands() -> list[tuple[str, str, _CommandRegister]]:
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
