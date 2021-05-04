# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Felipe Carlos.
#
# invenio-test-ext is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""An another InvenioRDM Extension example"""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from flask import Blueprint, render_template
from flask_babelex import gettext as _

#
# extension example
#
# blueprint = Blueprint(
#     'gkhext',
#     __name__,
#     template_folder='templates',
#     static_folder='static',
# )

# # @blueprint.route("/")
# def index():
#     """Render a basic view."""
#     return render_template(
#         "gkhext/index.html",
#         module_name=_('geo-knowledge-hub-ext'))

from typing import Dict

from invenio_search.api import RecordsSearch
from elasticsearch_dsl.utils import AttrDict


def generate_ui_bp(flask_app):
    routes = flask_app.config.get("MY_ROUTES")

    bp = Blueprint(
        'test_theme',
        __name__,
        template_folder="templates",
    )

    # This function creates a blueprint and associates it with 
    # the route name "test" configured in "MY_ROUTES
    bp.add_url_rule(routes.get("test"), view_func=test)

    @bp.app_template_filter("make_dict_like")
    def make_dict_like(value: str, key: str) -> Dict[str, str]:
        return {key: value}

    @bp.app_template_filter("cast_to_dict")
    def cast_to_dict(attr_dict):
        return AttrDict.to_dict(attr_dict)

    return bp


def test():
    # This function renders the test.html page

    # The HTML file is a jinja template. Its content is generated dynamically by 
    # creating sections using the passed records. The records that will be displayed are 
    # retrieved with the query made by the "RecordsSearch" class
    return render_template(
        "gkhext/test.html",
        invenio_records=RecordsSearch().sort("-created").execute()
    )


from invenio_app_rdm.records_ui.views.decorators import (
    pass_record_files,
    pass_record,
)
from invenio_rdm_records.resources.serializers import UIJSONSerializer



@pass_record
@pass_record_files
def record_detail(record=None, files=None, pid_value=None, is_preview=False):
    # This function renders the records page. It acts as a proxy. When the rendering is requested, 
    # the call passes through this function, which can make changes to the requested object.
    # These modifications can be adding new content, removing fields, and so on
    files_dict = None if files is None else files.to_dict()

    import json

    print(dir(record))
    print(record.to_dict())
    metadata = record.to_dict()["metadata"]

    if "related_identifiers" in metadata:
        print(record.to_dict()["metadata"]["related_identifiers"])

    return render_template(
        "gkhext/detail.html",
        record=UIJSONSerializer().serialize_object_to_dict(record.to_dict()),
        pid=pid_value,
        files=files_dict,
        permissions=record.has_permissions_to(['edit', 'new_version', 'manage',
                                               'update_draft', 'read_files']),
        is_preview=is_preview,
    )
