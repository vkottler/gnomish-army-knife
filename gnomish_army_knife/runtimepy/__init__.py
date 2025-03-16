"""
A module implementing runtimepy-related interfaces.
"""

# built-in
import asyncio
from pathlib import Path
from shutil import copytree

# third-party
from runtimepy.net.arbiter import AppInfo

# module under test
from gnomish_army_knife.net.connection import CombatLogEventConnection
from gnomish_army_knife.net.task import LogServerTask
from gnomish_army_knife.net.writer import LogWriterTask


async def peer_finish_then_copy(app: AppInfo) -> int:
    """A network application that doesn't do anything."""

    await asyncio.gather(
        *(proc.protocol.exited.wait() for proc in app.peers.values())
    )

    task = list(app.search_tasks(LogWriterTask))[0]

    if task.runtime.database.matchdb_path.is_dir():
        copytree(
            task.runtime.database.matchdb_path,
            Path(app.config_param("matchdb_dest", "tasks")).joinpath(
                "matchdb"
            ),
            dirs_exist_ok=True,
        )

    # Ensure connection clean-up handling runs.
    await task.wait_iterations(2.0, count=2)

    return 0


async def send_all_events(app: AppInfo) -> int:
    """A network application that doesn't do anything."""

    task = list(app.search_tasks(LogServerTask))[0]

    with app.log_time("Event queue initial event saturation", reminder=True):
        await task.queue_saturated.wait()

    # Relies on 'once' config.
    with app.log_time("Event queue fully flushed", reminder=True):
        while not await task.wait_for_disable(1.0):
            pass

    assert await list(app.search(kind=CombatLogEventConnection))[0].loopback()

    return 0
