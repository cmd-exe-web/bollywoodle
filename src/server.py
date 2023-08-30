from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
import os
from .controllers.controller import FetchClip
from .config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)

mongo = PyMongo(app)
db = mongo.db

api.add_resource(FetchClip, "/video/<string:video_key>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
