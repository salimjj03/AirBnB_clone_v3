#!/usr/bin/python3
""" This model Import a Blueprint. """

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
    """ This method Retutn json status code. """

    var = {"status": "ok"}
    return jsonify(var)


@app_views.route("/stats")
def stats():
    """ Thin method retrieves the number of each objects by type. """

    dic = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
            }
    return jsonify(dic)
