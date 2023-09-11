from ..models.video import Video


class VideoService:
    def get_video_by_key(self, video_key):
        video = Video.objects(s3_object_key=video_key).first()
        return video

    def get_all_videos(self):
        field_to_include = ["name", "s3_object_key"]
        videos = Video.objects().only(*field_to_include)
        return videos
