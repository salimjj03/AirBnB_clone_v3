#!/usr/bin/python3
""" Thi model Create a new view for State objects
that handles all default RESTFul API actions."""


from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.user import User


@app_views.route("/users", methods=["GET", "POST"])
@app_views.route("/users/", methods=["GET", "POST"])
def users():
    """ This method Retrieves the list of
    all State objects. """

    if request.method == "GET":
        ls = []
        all_users = storage.all("User")
        if all_users is not None:
            for key, value in all_users.items():
                ls.append(value.to_dict())

        return jsonify(ls)

    if request.method == "POST":
        req = request.get_json()
        if req is None:
            abort(400, "Not a JSON")
        if req.get("name") is None:
            abort(400, "Missing name")
        if req.get("password") is None:
            abort(400, "Missing password")
        if req.get("email") is None:
            abort(400, "Missing email")

        new_users = User(**req)
        new_users.save()
        return jsonify(new_users.to_dict()), 201


@app_views.route("/users/<s_id>", methods=["GET", "DELETE", "PUT"])
def user(s_id):
    """ This method Retrieves a State object. """

    obj = storage.get("User", s_id)
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
            obj.name = req.get("name")
            obj.name = req.get("password")
            obj.save()
            return jsonify(obj.to_dict()), 200

    abort(404)
