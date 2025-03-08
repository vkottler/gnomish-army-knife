"""
A module implementing a common runtime task base.
"""

# built-in
import argparse

# third-party
from runtimepy.net.arbiter import AppInfo
from runtimepy.net.arbiter.task import ArbiterTask
from runtimepy.primitives import Uint32

# internal
from gnomish_army_knife.runtime import GakRuntime


class GakRuntimeTask(ArbiterTask):
    """A class implementing a runtime environment for package tasks."""

    runtime: GakRuntime

    # Metrics.
    event_count: Uint32

    # No stateful elements are currently allocated during (runtime) init.
    auto_finalize = True

    def _init_state(self) -> None:
        """Add channels to this instance's channel environment."""

        self.event_count = Uint32()
        self.env.channel("event_count", self.event_count)

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)
        self._init_runtime(app)

    def _init_runtime(self, app: AppInfo) -> None:
        """Initialize package runtime."""

        # Parse command-line options and create the runtime instance.
        parser = argparse.ArgumentParser()
        GakRuntime.cli_args(parser)
        self.runtime = app.stack.enter_context(
            GakRuntime.create(
                parser.parse_args(
                    app.config.get(  # type: ignore
                        "gak_cli_args",
                        [],
                    )
                )
            )
        )
