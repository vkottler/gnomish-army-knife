"""
A module for working with schemas belonging to this package.
"""

# built-in
from typing import Optional as _Optional

# third-party
from vcorelib.dict.codec import DictCodec as _DictCodec
from vcorelib.schemas.base import SchemaMap as _SchemaMap
from vcorelib.schemas.json import JsonSchemaMap as _JsonSchemaMap

# internal
from gnomish_army_knife import PKG_NAME


class GakDictCodec(_DictCodec):
    """
    A simple wrapper for package classes that want to implement DictCodec.
    """

    default_schemas: _Optional[_SchemaMap] = _JsonSchemaMap.from_package(
        PKG_NAME.replace("-", "_")
    )
