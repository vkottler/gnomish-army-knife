# =====================================
# generator=datazen
# version=3.1.4
# hash=9488ecf11fb2f1e64e61f87cb9b1c7e6
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
        "3.11",
        "3.12",
    ],
}
setup(
    pkg_info,
    author_info,
)
