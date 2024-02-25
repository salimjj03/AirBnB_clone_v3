#!/usr/bin/python3
""" Thi model Create a new view for State objects
that handles all default RESTFul API actions."""


from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity


@app_views.route("/amenities", methods=["GET", "POST"])
@app_views.route("/amenities/", methods=["GET", "POST"])
def amenities():
    """ This method Retrieves the list of
    all State objects. """

    if request.method == "GET":
        ls = []
        all_amenities = storage.all("Amenity")
        if all_amenities is not None:
            for key, value in all_amenities.items():
                ls.append(value.to_dict())

        return jsonify(ls)

    if request.method == "POST":
        req = request.get_json()
        if req is None:
            abort(400, "Not a JSON")
        if req.get("name") is None:
            abort(400, "Missing name")

        new_amenity = Amenity(**req)
        new_amenity.save()
        return jsonify(new_amenity.to_dict()), 201


@app_views.route("/amenities/<s_id>", methods=["GET", "DELETE", "PUT"])
def amenity(s_id):
    """ This method Retrieves a State object. """

    obj = storage.get("Amenity", s_id)
    if obj is not None:
        if request.method == "GET":
            return jsonify(obj.to_dict())
        elif request.method == "DELETE":
            obj.delete()
            del obj
            return jsonify("{}"), 200
        elif request.method == "PUT":
            req = request.get_json()
            if req is None:
                abort(400, "Not a JSON")
            obj.name = req["name"]
            obj.save()
            return jsonify(obj.to_dict()), 200

    abort(404)
