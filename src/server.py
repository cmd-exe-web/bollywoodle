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

CORS(app)

db = MongoEngine(app)

api.add_resource(FetchClip, "/api/fetch-clip/<string:video_key>")
api.add_resource(ValidateGuess, "/api/validate-guess")
api.add_resource(AllVideosResource, "/api/videos")
api.add_resource(GetRandomVideoKey, "/api/get-random-video-key")
api.add_resource(VideoResource, "/api/video/<string:video_key>")
api.add_resource(OptionListResource, '/api/options')
api.add_resource(OptionResource, '/api/options/<string:option_id>')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
