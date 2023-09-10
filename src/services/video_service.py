from ..models.video import Video


class VideoService:
    def get_video_by_key(self, video_key):
        video = Video.objects(s3_object_key=video_key).first()
        return video
