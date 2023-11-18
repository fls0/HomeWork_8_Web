from mongoengine import connect
from models import Contact
from time import sleep

import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

def send_email(contact_id):
    print(f'Відправка емейлу контакту з ID {contact_id}...')
    sleep(2)
    print(f'Емейл відправлено контакту з ID {contact_id}.')

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')

    contact = Contact.objects(id=contact_id).first()

    if contact and not contact.message_sent:
        send_email(contact_id)

        contact.message_sent = True
        contact.save()

        print(f'Відмічено контакт {contact_id} як відправлено.')

channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
print('Очікування на повідомлення. Для виходу CTRL+C')
channel.start_consuming()
