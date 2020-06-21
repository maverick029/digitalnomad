# -*- coding: utf-8 -*-
"""Package __init__"""

VERSION_MAJOR = 0
VERSION_MINOR = 0
VERSION_PATCH = 1
VERSION_INFO = (VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH)
__version__ = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"

__all__ = [
    '__version__',
    'VERSION_MAJOR',
    'VERSION_MINOR',
    'VERSION_PATCH',
    'VERSION_INFO'
    ]
