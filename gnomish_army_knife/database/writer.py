"""
A module implementing an arena-match file-writing interface.
"""

# built-in
from typing import Optional

# third-party
import aiofiles
from vcorelib.io import ARBITER
from vcorelib.logging import LoggerMixin
from vcorelib.paths import Pathlike, normalize, rel

# internal
from gnomish_army_knife.database.event import CombatLogEvent
from gnomish_army_knife.database.meta import ArenaMatchMetadata
from gnomish_army_knife.enums.events import LogEvent


class ArenaMatchWriter(LoggerMixin):
    """A class capable of writing individual arena match events to disk."""

    def __init__(self, root: Pathlike) -> None:
        """Initialize this instance."""

        super().__init__()
        self.root = normalize(root)

        self.start_event: Optional[CombatLogEvent] = None
        self.bucket: list[str] = []
        self.meta = ArenaMatchMetadata()
        self._reset()

    def _reset(self) -> None:
        """Reset internal state."""

        # Could check for dropped events/loss at some point.
        self.bucket = []
        self.start_event = None

    async def _end_match(self) -> None:
        """Handle the end of a match."""

        path = self.meta.file_path(self.root)
        if self.bucket and path is not None and not path.is_file():
            path.parent.mkdir(parents=True, exist_ok=True)

            # Write event file.
            with self.log_time(
                "Writing '%s' (%d events) to '%s'",
                self.meta.summary,
                len(self.bucket),
                str(rel(path, base=self.root)),
            ):
                async with aiofiles.open(path, mode="w") as path_fd:
                    await path_fd.writelines(self.bucket)

            # Write metadata.
            with self.log_time("Writing metadata JSON"):
                await ARBITER.encode_async(
                    path.with_suffix(".json"), self.meta.data
                )

        self._reset()

    async def handle(self, event: CombatLogEvent) -> bool:
        """Returns true if the arena-match-writer consumed the event."""

        # Always check for a new start event.
        if event.name == LogEvent.MATCH_START:
            self._reset()
            self.start_event = event

        # Have a reference to a start event, this new event will
        # always be written.
        result = self.start_event is not None

        if result:
            self.bucket.append(event.line)
            if self.meta.handle(event):
                await self._end_match()

        return result
