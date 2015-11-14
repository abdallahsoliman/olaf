from os import environ
from django.core.management.base import BaseCommand, CommandError
from health.models import HeartRate

class Command(BaseCommand):
    help = "Deletes all heart rate values"

    def handle(self, *args, **options):

        if environ['DJANGO_SETTINGS_MODULE'] != "olaf.settings.dev":
            raise CommandError('This command can only be run in the development environment')

        HeartRate.objects.all().delete()
