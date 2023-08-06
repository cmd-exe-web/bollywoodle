from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_pymongo import PyMongo
import os

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


class HomeResource(Resource):
    def get(self):
        collection = db["user"]
        data = list(collection.find({}))
        for item in data:
            item["_id"] = str(item["_id"])

        return jsonify(data)


api.add_resource(HomeResource, "/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
