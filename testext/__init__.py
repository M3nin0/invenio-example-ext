# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Felipe Carlos.
#
# invenio-test-ext is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""An another InvenioRDM Extension example"""

from .ext import InvenioTestExt
from .version import __version__

__all__ = ('__version__', 'InvenioTestExt')
