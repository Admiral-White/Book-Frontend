import pika
import json
from .models import Book


def callback(ch, method, properties, body):
    print("Received message from RabbitMQ")
    book_data = json.loads(body)

    # Add book to frontend's catalog
    Book.objects.create(
        id=book_data['id'],
        title=book_data['title'],
        author=book_data['author'],
        publisher=book_data['publisher'],
        category=book_data['category'],
        is_borrowed=False
    )
    print(f"Added book: {book_data['title']}")


def consume_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare an exchange and queue
    channel.exchange_declare(exchange='library', exchange_type='topic')
    channel.queue_declare(queue='frontend_catalog')

    # Bind the queue to the exchange
    channel.queue_bind(exchange='library', queue='frontend_catalog', routing_key='book.added')

    # Set up the message consumer
    channel.basic_consume(queue='frontend_catalog', on_message_callback=callback, auto_ack=True)
    print("Waiting for messages from RabbitMQ...")

    channel.start_consuming()
