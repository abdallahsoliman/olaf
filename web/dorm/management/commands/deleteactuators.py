from os import environ
from django.core.management.base import BaseCommand, CommandError
from dorm.models import Actuator, ActuatorType

class Command(BaseCommand):
    help = "Deletes all actuators and actuator types. Only for development environment."

    def handle(self, *args, **options):

        if environ['DJANGO_SETTINGS_MODULE'] != "olaf.settings.dev":
            raise CommandError('This command can only be run in the development environment')

        Actuator.objects.all().delete()
        ActuatorType.objects.all().delete()
