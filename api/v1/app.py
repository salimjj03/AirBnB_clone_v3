#!/usr/bin/python3
""" This is the app module. """

from flask import Flask, make_response, jsonify
from os import getenv
from models import storage
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/*": {"origins": "http://0.0.0.0"}})


@app.teardown_appcontext
def teardown(exc):
    """ This is the teardown_appcontext. """

    storage.close()


@app.errorhandler(404)
def errorhandler(error):
    err = {"error": "Not found"}
    return make_response(jsonify(err), 404)


if __name__ == "__main__":
    h = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"
    p = getenv("HBNB_API_PORT") if getenv("HBNB_API_HOST") else 5000
    app.run(host=h, port=p, threaded=True)
