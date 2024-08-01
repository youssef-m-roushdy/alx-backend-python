#!/usr/bin/env python3
"""
    Safely get a value from a dictionary
"""
from typing import Any, Mapping, TypeVar, Optional, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any],
                     key: Any,
                     default: Optional[T] = None
                     ) -> Union[Any, T]:
    """
    Safely get a value from a dictionary
    """
    return dct.get(key, default)
