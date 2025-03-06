"""
A module implementing networking-related interfaces for the package.
"""

# third-party
from runtimepy.net.arbiter.task import TaskFactory
from runtimepy.net.arbiter.tcp import TcpConnectionFactory
from runtimepy.net.arbiter.websocket import WebsocketConnectionFactory
from runtimepy.net.tcp.connection import TcpConnection
from runtimepy.net.websocket import WebsocketConnection

# internal
from gnomish_army_knife.net.connection import CombatLogEventConnection
from gnomish_army_knife.net.task import LogServerTask
from gnomish_army_knife.net.writer import LogWriterTask

__all__ = [
    "CombatLogEventConnection",
    "LogServer",
    "LogWriter",
    "TcpCombatLogEvent",
    "WebsocketCombatLogEvent",
    "WebsocketCombatLogEventConnection",
    "TcpCombatLogEventConnection",
]


class LogServer(TaskFactory[LogServerTask]):
    """A class implementing a log-server task factory."""

    kind = LogServerTask


class LogWriter(TaskFactory[LogWriterTask]):
    """A class implementing a log-writer task factory."""

    kind = LogWriterTask


class WebsocketCombatLogEventConnection(
    CombatLogEventConnection, WebsocketConnection
):
    """WebSocket combat-log connection."""


class TcpCombatLogEventConnection(CombatLogEventConnection, TcpConnection):
    """TCP combat-log connection."""


class TcpCombatLogEvent(TcpConnectionFactory[TcpCombatLogEventConnection]):
    """TCP JSON-connection factory."""

    kind = TcpCombatLogEventConnection


class WebsocketCombatLogEvent(
    WebsocketConnectionFactory[WebsocketCombatLogEventConnection]
):
    """WebSocket combat-log-connection factory."""

    kind = WebsocketCombatLogEventConnection
