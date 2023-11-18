from models import Contact
from faker import Faker

import pika

fake = Faker()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

for _ in range(15):
    contact = Contact(
        fullname=fake.name(),
        email=fake.email(),
        message_sent=False
    )
    contact.save()

    channel.basic_publish(
        exchange='', routing_key='email_queue', body=str(contact.id))
    
connection.close()
