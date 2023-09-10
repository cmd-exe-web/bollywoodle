from mongoengine import Document, StringField, URLField


class Video(Document):
    name = StringField(required=True, unique=True)
    url = URLField(required=False)
    s3_object_key = StringField(required=True, unique=True)
