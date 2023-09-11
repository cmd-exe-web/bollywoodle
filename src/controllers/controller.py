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


class AllVideosResource(Resource):
    def get(self):
        videos = VideoService().get_all_videos()

        formatted_videos = [{"name": video.name,
                             "key": video.s3_object_key} for video in videos]

        return formatted_videos, 200


class GetRandomVideoKey(Resource):
    def get(self):
        random_video_key = VideoService().get_random_video_key()
        if random_video_key:
            return {'key': random_video_key}, 200
        else:
            return {'message': 'No videos available'}, 404
