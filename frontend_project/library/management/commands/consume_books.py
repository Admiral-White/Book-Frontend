from django.core.management.base import BaseCommand
from library.rabbitmq import consume_message


class Command(BaseCommand):
    help = 'Start RabbitMQ consumer for frontend'

    def handle(self, *args, **kwargs):
        consume_message()
