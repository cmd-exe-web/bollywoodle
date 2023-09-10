from flask import Response, request
from flask_restful import Resource
import json
from ..services.s3_service import S3Service
from ..services.video_service import VideoService


class FetchClip(Resource):
    def get(self, video_key):
        try:
            video_stream = S3Service().get_object(video_key)

            return Response(
                video_stream.iter_chunks(chunk_size=4096), mimetype="video/mp4"
            )
        except Exception as e:
            return str(e), 404


class ValidateGuess(Resource):
    def get(self):
        guess = request.args.get('guess')
        video_key = request.args.get('key')

        print(guess)
        print(video_key)

        video_service = VideoService()
        video = video_service.get_video_by_key(video_key).to_json()
        data = json.loads(video)
        video_name = data["name"]

        if guess == video_name:
            print("Is correct cnd ran")
            print(True)
            response = {"valid": True}
            valid_json = json.dumps(response)
            return valid_json, 200
        else:
            print("Isnt correct cnd ran")
            print(False)
            response = {"valid": False}
            invalid_json = json.dumps(response)
            return invalid_json, 200
