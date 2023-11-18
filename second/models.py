from mongoengine import connect, StringField, BooleanField, Document, EmailField, IntField

connect(
    db="homework-producer-consumer",
    host="mongodb+srv://sadurskyim:123123q@flsx.tisgnah.mongodb.net/?retryWrites=true&w=majority",
)

class Contact(Document):
    fullname = StringField(required=True, unique=True)
    email = EmailField()
    message_sent = BooleanField(default=False)