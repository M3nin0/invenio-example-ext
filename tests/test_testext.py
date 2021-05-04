# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Felipe Carlos.
#
# invenio-test-ext is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Module tests."""

from flask import Flask

from testext import InvenioTestExt


def test_version():
    """Test version import."""
    from testext import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = InvenioTestExt(app)
    assert 'invenio-test-ext' in app.extensions

    app = Flask('testapp')
    ext = InvenioTestExt()
    assert 'invenio-test-ext' not in app.extensions
    ext.init_app(app)
    assert 'invenio-test-ext' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to invenio-test-ext' in str(res.data)
