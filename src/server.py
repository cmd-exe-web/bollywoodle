from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_mongoengine import MongoEngine
from .controllers.video_controller import FetchClip, ValidateGuess, AllVideosResource, GetRandomVideoKey, VideoResource
from .controllers.option_controller import OptionListResource, OptionResource
from .config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app)

db = MongoEngine(app)

cors = CORS(app, resources={
    r"/fetch-clip/*": {"origins": "http://localhost:5173"},
    r"/validate-guess*": {"origins": "http://localhost:5173"},
    r"/videos": {"origins": "http://localhost:5173"},
    r"/get-random-video-key": {"origins": "http://localhost:5173"},
    r"/video/*": {"origins": "http://localhost:5173"},
    r"/options": {"origins": "http://localhost:5173"},
    r"/options/*": {"origins": "http://localhost:5173"},
})

api.add_resource(FetchClip, "/fetch-clip/<string:video_key>")
api.add_resource(ValidateGuess, "/validate-guess")
api.add_resource(AllVideosResource, "/videos")
api.add_resource(GetRandomVideoKey, "/get-random-video-key")
api.add_resource(VideoResource, "/video/<string:video_key>")
api.add_resource(OptionListResource, '/options')
api.add_resource(OptionResource, '/options/<string:option_id>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
