#!/usr/bin/python3
""" This is the app module. """

from flask import Flask
from os import getenv
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exc):
    """ This is the teardown_appcontext. """

    storage.close()


if __name__ == "__main__":
    h = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"
    p = getenv("HBNB_API_PORT") if getenv("HBNB_API_HOST") else 5000
    app.run(host=h, port=p, threaded=True)
