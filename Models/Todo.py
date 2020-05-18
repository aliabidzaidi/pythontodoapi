from mongoengine import *
import datetime

# Classes are just blueprint for the objects
class Todo(Document):
    heading = StringField(required=True)
    body = StringField(required=True)
    colorCode = StringField(default="primary")
    dateAdded = DateTimeField(default=datetime.datetime.now())
    dateUpdated = DateTimeField(default=None)

    def asdict(self):
        return {'id': str(self.id), 'heading': self.heading, 'body': self.body, 'colorCode': self.colorCode, 
                    'dateAdded': self.dateAdded, 'dateUpdated': self.dateUpdated}

