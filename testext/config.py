# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Felipe Carlos.
#
# invenio-test-ext is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""An another InvenioRDM Extension example"""

# TODO: This is an example file. Remove it if your package does not use any
# extra configuration variables.

INVENIO_TEST_EXT_DEFAULT_VALUE = 'foobar'
"""Default value for the application."""

INVENIO_TEST_EXT_BASE_TEMPLATE = 'testext/base.html'
"""Default base template for the demo page."""

# The "MY_ROUTES" dictionary will be used to associate a route with a name. 
# In code execution this is used to define on which route the created functions will take effect
MY_ROUTES = {
    "test": "/test-route"
}
