from ..models.video import Video
import random


class VideoService:
    def get_video_by_key(self, video_key):
        video = Video.objects(s3_object_key=video_key).first()
        return video

    def get_all_videos(self):
        field_to_include = ["name", "s3_object_key"]
        videos = Video.objects().only(*field_to_include)
        return videos

    def get_random_video_key(self):
        videos = self.get_all_videos()
        if videos:
            random_video = random.choice(videos)
            return random_video.s3_object_key
        else:
            return None
