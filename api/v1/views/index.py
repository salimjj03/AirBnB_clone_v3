#!/usr/bin/python3
""" This model Import a Blueprint. """

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status")
def status():
    """ This method Retutn json status code. """

    var = {"status": "ok"}
    return jsonify(var)
