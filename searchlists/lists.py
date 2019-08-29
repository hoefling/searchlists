"""
Create String

DESCRIPTION
This module contains the create_string function that will take a list of items
and convert it to a single string.

This string can then be copied to the system clipboard.
"""

import pyperclip


def copy(*args, **kwargs):
    """
    copy will add the formatted string to the clipboard

    PARAMETERS
      passed directly to the create_string function as
      create_string(*args, **kwargs)

    RETURN None
    """
    pyperclip.copy(create_string(*args, **kwargs))


def create_string(items, quote=False, prefix=None, suffix=None, sep=" "):
    """
    create_string converts a list of items to a single string

    PARAMETERS
      items: list: list of items to convert to string
      quote: bool: (quote=False) whether or not the items should be quoted
      prefix: str|None: prefix to add to each item
      suffix: str|None: suffix to add to each item
      sep: str: the separator for each item

    RETURNS
     str: concatenation of each item

    RAISES
     TypeError
    """

    # validation
    if not isinstance(items, list):
        raise TypeError("items must be type list")
    if not isinstance(prefix, (str, type(None))):
        raise TypeError("prefix must be type str or None")
    if not isinstance(suffix, (str, type(None))):
        raise TypeError("suffix must be of type str or None")
    if not isinstance(sep, str):
        raise TypeError("sep must be a string")

    # add prefix and suffix and quotes where applicable
    if prefix is not None:
        items = [f"{prefix}{item}" for item in items]
    if suffix is not None:
        items = [f"{item}{suffix}" for item in items]
    if quote:
        items = [f'"{item}"' for item in items]

    return sep.join([str(k) for k in items])
