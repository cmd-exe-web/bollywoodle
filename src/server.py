from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_mongoengine import MongoEngine
from .controllers.controller import FetchClip, ValidateGuess
from .config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)

db = MongoEngine(app)

cors = CORS(app, resources={
    r"/video/*": {"origins": "http://localhost:5173"},
    r"/validate-guess*": {"origins": "http://localhost:5173"}
})

api.add_resource(FetchClip, "/video/<string:video_key>")
api.add_resource(ValidateGuess, "/validate-guess")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
