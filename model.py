from mongoengine import Document, StringField, DateTimeField



class Link(Document):
    url = StringField()
    expired_date = DateTimeField()
    hash = StringField()
