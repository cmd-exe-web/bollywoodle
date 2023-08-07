from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
import os
from .controllers.controller import FetchClip

app = Flask(__name__)
api = Api(app)


app.config["MONGO_URI"] = (
    "mongodb://"
    + os.environ["MONGODB_USERNAME"]
    + ":"
    + os.environ["MONGODB_PASSWORD"]
    + "@"
    + os.environ["MONGODB_HOSTNAME"]
    + ":27017/"
    + os.environ["MONGODB_DATABASE"]
    + "?authSource=admin"
)

mongo = PyMongo(app)
db = mongo.db


api.add_resource(FetchClip, "/video/<string:video_key>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
