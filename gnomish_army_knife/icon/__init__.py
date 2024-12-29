"""
A module implementing icon-related interfaces.
"""

ICON_FSTR = "![icon](https://render.worldofwarcraft.com/us/icons/56/{}.jpg)"

# Keep in sync with schema default.
DEFAULT_ICON = "inv_misc_questionmark"


def icon_url(icon: str = DEFAULT_ICON) -> str:
    """Get an icon URL."""
    return ICON_FSTR.format(icon)
