"""
A module implementing a user interface task that consumes combat event
messages.
"""

# built-in
import asyncio
from pathlib import Path
from queue import Queue

# third-party
from runtimepy.net.arbiter import AppInfo
from runtimepy.net.arbiter.task import TaskFactory
from vcorelib.asyncio.cli import ProcessResult, run_command
from vcorelib.logging import LoggerType

# internal
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.enums.events import LogEvent
from gnomish_army_knife.net.connection import CombatLogEventConnection
from gnomish_army_knife.runtime.task import GakRuntimeTask

SOUND_BASE = Path("/opt/libre-embedded/mnt/8TB_mirrored_mechanical_0/audacity")


async def play_sound_effect(
    logger: LoggerType, name: str
) -> asyncio.Task[ProcessResult]:
    """Play a sound effect."""

    task = asyncio.create_task(
        run_command(logger, "aplay", str(SOUND_BASE.joinpath(f"{name}.wav")))
    )
    await asyncio.sleep(0)
    return task


# need to get names of all pvp zones (probably a good internet source)
FILM_IN_ZONE = {"Tol'viron Arena"}


class UiTask(GakRuntimeTask):
    """A class that manages user-interface interactions."""

    queues: dict[CombatLogEventConnection, tuple[Queue[CombatLogEvent], int]]

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)
        self.queues = {}

    async def start_recording(self) -> None:
        """Attempt to start recording."""

        # check if currently recording

        self.logger.info("START RECORDING (if not)")
        # await (await play_sound_effect(self.logger, "start_recording"))

    async def stop_recording(self) -> None:
        """Attempt to stop recording."""

        # check if currently recording

        self.logger.info("STOP RECORDING (if)")
        # await (await play_sound_effect(self.logger, "stop_recording"))

    async def dispatch(self) -> bool:
        """Dispatch an iteration of this task."""

        # log some info when connection state changed

        # essentially copied from LogWriterTask
        inactive = set()
        active = set()
        for conn in self.app.conn_manager.by_type(CombatLogEventConnection):
            active.add(conn)
            if conn not in self.queues:
                queue: Queue[CombatLogEvent] = Queue()
                self.queues[conn] = (queue, conn.queue.register(queue))
                conn.logger.info("Registered as UI event stream.")
        for conn in self.queues:
            if conn not in active:
                inactive.add(conn)
        for conn in inactive:
            conn.queue.remove(self.queues[conn][1])
            del self.queues[conn]

        # get events
        for queue, _ in self.queues.values():
            if not queue.empty():
                tasks = []

                # await (await play_sound_effect(self.logger, "telegram"))

                while not queue.empty():
                    event = queue.get_nowait()

                    match event.name:
                        case LogEvent.MATCH_START:
                            await self.start_recording()
                            tasks.append(
                                await play_sound_effect(
                                    self.logger, "match_start"
                                )
                            )

                        case LogEvent.COMBATANT_INFO:
                            await self.start_recording()
                            tasks.append(
                                await play_sound_effect(
                                    self.logger, "combatant_info"
                                )
                            )

                        case LogEvent.MATCH_END:
                            await self.stop_recording()
                            tasks.append(
                                await play_sound_effect(
                                    self.logger, "match_end"
                                )
                            )

                        case LogEvent.ZONE_CHANGE:
                            zone = event.data[1].replace('"', "")
                            if zone in FILM_IN_ZONE:
                                await self.start_recording()
                            else:
                                await self.stop_recording()

                            tasks.append(
                                await play_sound_effect(
                                    self.logger, "zone_change"
                                )
                            )

                            self.logger.info(
                                "Detected zone change to '%s'.", zone
                            )

                        case _:
                            self.ignore_count.increment()

                # tasks.append(await play_sound_effect(self.logger, "stop"))

                await asyncio.gather(*tasks)

        return True


class GakUi(TaskFactory[UiTask]):
    """A class implementing a log-writer task factory."""

    kind = UiTask
