"""
A module implementing networking-related interfaces for the package.
"""

# third-party
from runtimepy.net.arbiter.task import TaskFactory

# internal
from gnomish_army_knife.net.connection import CombatLogEventConnection
from gnomish_army_knife.net.task import LogServerTask

__all__ = ["CombatLogEventConnection", "LogServer"]


class LogServer(TaskFactory[LogServerTask]):
    """A class implementing a log-server task factory."""

    kind = LogServerTask
