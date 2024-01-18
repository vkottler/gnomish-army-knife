# =====================================
# generator=datazen
# version=3.1.4
# hash=e6e639b230520a9b62aa06e0861d6555
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
from gnomish_army_knife.commands.scan import add_scan_cmd


def commands() -> _List[_Tuple[str, str, _CommandRegister]]:
    """Get this package's commands."""

    return [
        (
            "scan",
            "scan the 'World of Warcraft' directory for updates",
            add_scan_cmd,
        ),
        ("noop", "command stub (does nothing)", lambda _: lambda _: 0),
    ]
