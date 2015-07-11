from os import environ
from django.core.management.base import BaseCommand, CommandError
from authenticate.models import User

class Command(BaseCommand):
    help = "Creates 'x' new users. Only for development environment."

    def handle(self, *args, **options):

        if environ['DJANGO_SETTINGS_MODULE'] != "olaf.settings.dev":
            raise CommandError('This command can only be run in the development environment')

        User.objects.all().delete()
