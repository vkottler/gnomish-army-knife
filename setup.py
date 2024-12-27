# =====================================
# generator=datazen
# version=3.2.0
# hash=7e154dbc4dcc906993a41502a02d7357
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
    "email": "vaughn@libre-embedded.com",
    "username": "vkottler",
}
pkg_info = {
    "name": PKG_NAME,
    "slug": PKG_NAME.replace("-", "_"),
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.12",
        "3.13",
    ],
}
setup(
    pkg_info,
    author_info,
)
