"""
A module implementing a simple queue-handler event interface.
"""

# built-in
from contextlib import contextmanager
from queue import Queue
from typing import Iterator

# internal
from gnomish_army_knife.database.event import CombatLogEvent


class CombatLogQueueHandler:
    """
    A simple mixin class for handling combat log events via per-event handlers
    and queue handlers.
    """

    def __init__(self) -> None:
        """Initialize this instance."""

        self.queues: dict[int, Queue[CombatLogEvent]] = {}
        self.queue_idx = 1

    def register(self, queue: Queue[CombatLogEvent]) -> int:
        """Register a queue."""

        result = self.queue_idx
        self.queues[result] = queue
        self.queue_idx += 1
        return result

    def remove(self, index: int) -> bool:
        """Remove a previously registered queue."""

        remove = index in self.queues
        if remove:
            del self.queues[index]
        return remove

    @contextmanager
    def registered(self, queue: Queue[CombatLogEvent]) -> Iterator[None]:
        """Register a queue as a managed context."""

        idx = self.register(queue)
        try:
            yield
        finally:
            assert self.remove(idx)

    def handle(self, event: CombatLogEvent) -> None:
        """Handle a combat-log event."""
        for queue in self.queues.values():
            queue.put_nowait(event)
