# =====================================
# generator=datazen
# version=3.1.4
# hash=85faa5f531f6c51bf6c6a3204a4e9d9f
# =====================================

"""
gnomish-army-knife - Package definition for distribution.
"""

# third-party
try:
    from setuptools_wrapper.setup import setup
except (ImportError, ModuleNotFoundError):
    from gnomish_army_knife_bootstrap.setup import setup  # type: ignore

# internal
from gnomish_army_knife import DESCRIPTION, PKG_NAME, VERSION

author_info = {
    "name": "Vaughn Kottler",
    "email": "vaughnkottler@gmail.com",
    "username": "vkottler",
}
pkg_info = {
    "name": PKG_NAME,
    "slug": PKG_NAME.replace("-", "_"),
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.8",
        "3.9",
        "3.10",
        "3.11",
    ],
}
setup(
    pkg_info,
    author_info,
)
