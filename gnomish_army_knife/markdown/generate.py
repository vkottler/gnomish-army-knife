"""
A module implementing a markdown-generation entry interface.
"""

# built-in
from pathlib import Path


def entry(output: Path) -> None:
    """Entry for markdown generation."""

    # create output dir, load data, make index.md + class-specific pages?
    output.mkdir(parents=True, exist_ok=True)

    # schema + schema object for macros. could be neat at some point to be
    # able to auto-generate HTML forms for these
