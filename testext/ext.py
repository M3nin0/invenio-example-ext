# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Felipe Carlos.
#
# invenio-test-ext is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""An another InvenioRDM Extension example"""

from flask_babelex import gettext as _

from . import config

from .views import test
from .views import record_detail


class InvenioTestExt(object):
    """invenio-test-ext extension."""

    def __init__(self, app=None):
        """Extension initialization."""
        # TODO: This is an example of translation string with comment. Please
        # remove it.
        # NOTE: This is a note to a translator.
        _('A translation string')
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Flask application initialization."""

        # This part of the code handles the application's routes: 

        # 1st: The addition of the new route, /test-route, is performed. When this 
        # route is requested by users the function "test" will be used to render the page.
        app.add_url_rule("/test-route", "test-route", test)

        # 2°: The default /records route is overwritten. So, when the user calls 
        # the /records route passing a pid_value, the function "record_detail" will be used to render the page
        app.add_url_rule("/records/<pid_value>", "test-record-detail", record_detail)

        self.init_config(app)
        app.extensions['invenio-test-ext'] = self

    def init_config(self, app):
        """Initialize configuration."""
        # Use theme's base template if theme is installed
        if 'BASE_TEMPLATE' in app.config:
            app.config.setdefault(
                'INVENIO_TEST_EXT_BASE_TEMPLATE',
                app.config['BASE_TEMPLATE'],
            )
        for k in dir(config):
            if k.startswith('INVENIO_TEST_EXT_'):
                app.config.setdefault(k, getattr(config, k))
