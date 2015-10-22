from os import environ
from django.core.management.base import BaseCommand, CommandError
from dorm.factories import ActuatorFactory

class Command(BaseCommand):
    help = "Creates 'x' new actuators. Only for development environment."

    def add_arguments(self, parser):
        parser.add_argument('num_actuators', type=int, help="number of actuators to create")

    def handle(self, *args, **options):

        if environ['DJANGO_SETTINGS_MODULE'] != "olaf.settings.dev":
            raise CommandError('This command can only be run in the development environment')

        ActuatorFactory.create_batch(options['num_actuators'])
