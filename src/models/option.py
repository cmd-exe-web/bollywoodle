from mongoengine import Document, StringField


class Option(Document):
    name = StringField(required=True, unique=True)
