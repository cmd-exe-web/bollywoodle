import boto3
import os

access_key_id = os.getenv("S3_ACCESS_KEY")
secret_access_key = os.getenv("SECRET_ACCESS_KEY")
region_name = "ap-south-1"

s3_resource = boto3.resource(
    "s3",
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    region_name=region_name,
)
