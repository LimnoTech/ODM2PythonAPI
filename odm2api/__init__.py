from __future__ import (absolute_import, division, print_function)

from odm2api.base import init_api

__all__ = [
    'init_api'
]

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
