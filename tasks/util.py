"""
A module implementing runtimepy utilities.
"""

# built-in
from pathlib import Path

# third-party
from runtimepy.net.arbiter.config import ConfigObject
from runtimepy.net.server import RuntimepyServerConnection

# internal
from gnomish_army_knife.macro.database import DEFAULT_OUT


def add_web_server_paths(_: ConfigObject) -> None:
    """Add some disk paths to runtimepy's HTTP server."""

    # Add markdown sources.
    for path in [Path(DEFAULT_OUT)]:
        if path not in RuntimepyServerConnection.class_paths:
            RuntimepyServerConnection.class_paths.append(path)
