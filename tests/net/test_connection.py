"""
Test the 'net.connection' module.
"""

# built-in
import asyncio
import os
from pathlib import Path
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
from gnomish_army_knife.net.task import LogServerTask

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
                await asyncio.sleep(0.1)

            assert queue.get_nowait()

    task = list(app.search_tasks(LogServerTask))[0]
    await task.wait_iterations(40.0, count=2)

    return 0


def test_combat_log_event_connection():
    """Test the combat-log event server."""

    os.environ["PYTHONPATH"] = (
        f"{Path().resolve()}:{os.environ.get('PYTHONPATH', "")}"
    )

    assert (
        runtimepy_main(
            [
                PKG_NAME,
                "-C",
                str(resource(DEFAULT_CONFIG).parent),
                "arbiter",
                # was 'server_test.yaml'
                "combined_test.yaml",
            ]
        )
        == 0
    )
