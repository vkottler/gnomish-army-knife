"""
Test the 'net.connection' module.
"""

# built-in
from asyncio import sleep
from queue import Queue

# third-party
from runtimepy import PKG_NAME
from runtimepy.entry import main as runtimepy_main
from runtimepy.net.arbiter import AppInfo

# module under test
from gnomish_army_knife import DEFAULT_CONFIG
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.net import (
    TcpCombatLogEventConnection,
    WebsocketCombatLogEventConnection,
)

# internal
from tests.resources import resource


async def conn_test(app: AppInfo) -> int:
    """Waits for the stop signal to be set."""

    # Test that we receive events via the client connections.
    for client in [
        app.single(pattern="client", kind=WebsocketCombatLogEventConnection),
        app.single(pattern="client", kind=TcpCombatLogEventConnection),
    ]:
        queue: Queue[CombatLogEvent] = Queue()
        with client.queue.registered(queue):
            # Wait for the queue to have something.
            while queue.empty():
                await sleep(0.1)

            assert queue.get_nowait()

    return 0


def test_combat_log_event_connection():
    """Test the combat-log event server."""

    assert (
        runtimepy_main(
            [
                PKG_NAME,
                "-C",
                str(resource(DEFAULT_CONFIG).parent),
                "arbiter",
                "server_test.yaml",
            ]
        )
        == 0
    )
