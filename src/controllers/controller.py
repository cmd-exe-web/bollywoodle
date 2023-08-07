from flask import Response
from flask_restful import Resource
from ..services.s3_service import S3Service


class FetchClip(Resource):
    def get(self, video_key):
        try:
            video_stream = S3Service().get_object(video_key)

            return Response(
                video_stream.iter_chunks(chunk_size=4096), mimetype="video/mp4"
            )
        except Exception as e:
            return str(e), 404
