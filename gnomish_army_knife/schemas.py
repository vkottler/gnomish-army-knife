"""
A module for working with schemas belonging to this package.
"""

# built-in
from typing import Optional as _Optional

# third-party
from vcorelib.dict.codec import DictCodec as _DictCodec
from vcorelib.io import DEFAULT_INCLUDES_KEY
from vcorelib.io.markdown import MarkdownMixin
from vcorelib.paths.find import PACKAGE_SEARCH
from vcorelib.schemas.base import SchemaMap as _SchemaMap
from vcorelib.schemas.json import JsonSchemaMap as _JsonSchemaMap

# internal
from gnomish_army_knife import PKG_SLUG

# Add this package to the search path.
if PKG_SLUG not in PACKAGE_SEARCH:
    PACKAGE_SEARCH.insert(0, PKG_SLUG)


class GakDictCodec(_DictCodec, MarkdownMixin):
    """
    A simple wrapper for package classes that want to implement DictCodec.
    """

    default_schemas: _Optional[_SchemaMap] = _JsonSchemaMap.from_package(
        PKG_SLUG, includes_key=DEFAULT_INCLUDES_KEY
    )
