"""
Test the 'net.writer' module.
"""

# third-party
from runtimepy import PKG_NAME
from runtimepy.entry import main as runtimepy_main
from runtimepy.net.arbiter import AppInfo

# module under test
from gnomish_army_knife import DEFAULT_CONFIG
from gnomish_army_knife.net import TcpCombatLogEventConnection
from gnomish_army_knife.net.writer import LogWriterTask

# internal
from tests.resources import resource


async def writer_test(app: AppInfo) -> int:
    """Waits for the stop signal to be set."""

    task = list(app.search_tasks(LogWriterTask))[0]

    client = await TcpCombatLogEventConnection.create_connection(
        host="localhost", port=app.ports["tcp_combat_log"]
    )
    async with client.process_then_disable(stop_sig=app.stop):
        # Wait for connection to initialize.
        await client.initialized.wait()

        await task.wait_iterations(2.0, count=2)

        # do tests (feed events over client side of connection)

    await task.wait_iterations(2.0, count=2)

    return 0


def test_combat_log_event_writer():
    """Test the combat-log writer task."""

    assert (
        runtimepy_main(
            [
                PKG_NAME,
                "-C",
                str(resource(DEFAULT_CONFIG).parent),
                "arbiter",
                "writer_test.yaml",
            ]
        )
        == 0
    )
