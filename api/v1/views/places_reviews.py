#!/usr/bin/python3
""" Thi model Create a new view for State objects
that handles all default RESTFul API actions."""


from flask import jsonify, abort, request
from models import storage
from api.v1.views import app_views
from models.review import Review


@app_views.route("/places/<place_id>/reviews", methods=["GET", "POST"])
@app_views.route("/places/<place_id>/reviews/", methods=["GET", "POST"])
def reviews(place_id):
    """ This method Retrieves the list of
    all State objects. """

    if storage.get("Place", place_id) is None:
        abort(404)
    if request.method == "GET":
        ls = []
        all_review = storage.all("Review")
        for key, value in all_review.items():
            if value.place_id == place_id:
                ls.append(value.to_dict())

        return jsonify(ls)

    if request.method == "POST":
        req = request.get_json()
        if req is None:
            abort(400, "Not a JSON")
        if req.get("user_id") is None:
            abort(400, "Missing user_id")
        if storage.get("User", req.get("user_id")) is None:
            abort(404)
        if req.get("text") is None:
            abort(400, "Missing text")

        new_state = Place(**req)
        new_state.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route("/reviews/<review_id>", methods=["GET", "DELETE", "PUT"])
def review(review_id):
    """ This method Retrieves a State object. """

    obj = storage.get("Review", review_id)
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
            else:
                obj.name = req["name"]
                obj.save()
                return jsonify(obj.to_dict()), 200

    abort(404)
