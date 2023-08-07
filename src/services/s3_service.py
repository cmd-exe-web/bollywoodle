from ..config import s3_resource
from ..constants import CLIP_BUCKET_NAME


class S3Service:
    def __init__(self, bucket_name=CLIP_BUCKET_NAME):
        self.bucket_name = bucket_name
        self.s3_resource = s3_resource

    def get_all_object_names(self):
        bucket = self.s3_resource.Bucket(self.bucket_name)

        object_names = [obj.key for obj in bucket.objects.all()]
        return object_names

    def get_object(self, object_name):
        s3_object = self.s3_resource.Object(self.bucket_name, object_name)
        return s3_object.get()["Body"]
