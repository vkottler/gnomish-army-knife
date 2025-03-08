"""
A module implementing a database interface for the package.
"""

# built-in
from contextlib import ExitStack
from pathlib import Path

# third-party
from vcorelib.logging import LoggerMixin

# internal
from gnomish_army_knife.database.combat_log import CombatLogState
from gnomish_army_knife.database.writer import ArenaMatchWriter


class ArenaMatchDb(LoggerMixin):
    """A class implementing a top-level program database interface."""

    ext = "json"

    def __init__(self, stack: ExitStack, root: Path) -> None:
        """Initialize this instance."""

        LoggerMixin.__init__(self)
        self.root = root

        self.logger.info("Loading state from '%s'.", self.root)

        # Load file-processing state.
        self.logs = stack.enter_context(
            CombatLogState.file_cache(self.combat_log_state_path)
        )

    def create_writer(self, subdir: str = "matchdb") -> ArenaMatchWriter:
        """Create an arena-match writer interface."""
        return ArenaMatchWriter(self.root.joinpath(subdir))

    def data_path(self, name: str) -> Path:
        """Get the path to a data file."""
        return self.root.joinpath(f"{name}.{self.ext}")

    @property
    def combat_log_state_path(self) -> Path:
        """Get the path to the combat-log state data."""
        return self.data_path("combat_log_state")
