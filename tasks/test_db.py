"""
A module implementing test data utilities.
"""

# built-in
import asyncio

# third-party
from runtimepy.net.arbiter.info import AppInfo

# internal
from gnomish_army_knife.net.connection import CombatLogEventConnection
from gnomish_army_knife.net.task import LogServerTask


async def peer_finish(app: AppInfo) -> int:
    """A network application that doesn't do anything."""

    await asyncio.gather(
        *(proc.protocol.exited.wait() for proc in app.peers.values())
    )

    return 0


async def write_db(app: AppInfo) -> int:
    """A network application that doesn't do anything."""

    task = list(app.search_tasks(LogServerTask))[0]

    with app.log_time("Event queue initial event saturation", reminder=True):
        await task.queue_saturated.wait()

    # Relies on 'once' config.
    with app.log_time("Event queue fully flushed", reminder=True):
        while not await task.wait_for_disable(1.0):
            pass

    conn = list(app.search(kind=CombatLogEventConnection))[0]

    with app.log_time("Connection loopback test", reminder=True):
        while not await conn.loopback():
            pass

    return 0
