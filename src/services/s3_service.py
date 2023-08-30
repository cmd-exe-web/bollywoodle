import os
import boto3
from ..constants import CLIP_BUCKET_NAME



class S3Service:
    def __init__(self, bucket_name=CLIP_BUCKET_NAME):
        self.bucket_name = bucket_name
        access_key_id = os.environ.get("AWS_ACCESS_KEY")
        secret_access_key = os.environ.get("AWS_SECRET_KEY")
        region_name = "ap-south-1"

        s3_resource = boto3.resource(
            "s3",
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            region_name=region_name,
        )

        self.s3_resource = s3_resource

    def get_all_object_names(self):
        bucket = self.s3_resource.Bucket(self.bucket_name)

        object_names = [obj.key for obj in bucket.objects.all()]
        return object_names

    def get_object(self, object_name):
        s3_object = self.s3_resource.Object(self.bucket_name, object_name)
        return s3_object.get()["Body"]
