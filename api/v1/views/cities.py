#!/usr/bin/python3
""" Thi model Create a new view for State objects
that handles all default RESTFul API actions."""


from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.state import City


@app_views.route("/states/<state_id>/cities", methods=["GET", "POST"])
@app_views.route("/states/<state_id>/cities/", methods=["GET", "POST"])
def city(state_id):
    """ This method Retrieves the list of
    all State objects. """

    if request.method == "GET":
        if storage.get("State", state_id) is None:
            abort(404)
        ls = []
        all_city = storage.all("City")
        for key, value in all_city.items():
            if value.state_id == state_id:
                ls.append(value.to_dict())

        return jsonify(ls)

    if request.method == "POST":
        req = request.get_json()
        if req is None:
            abort(400, "Not a JSON")
        if req.get("name") is None:
            abort(400, "Missing name")

        new_state = City(**req)
        new_state.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route("/cities/<city_id>", methods=["GET", "DELETE", "PUT"])
def state(city_id):
    """ This method Retrieves a State object. """

    obj = storage.get("City", city_id)
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
