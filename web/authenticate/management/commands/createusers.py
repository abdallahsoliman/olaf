from os import environ
from django.core.management.base import BaseCommand, CommandError
from authenticate.factories import UserFactory

class Command(BaseCommand):
    help = "Creates 'x' new users. Only for development environment."

    def add_arguments(self, parser):
        parser.add_argument('num_users', type=int, help="number of users to create")

    def handle(self, *args, **options):

        if environ['DJANGO_SETTINGS_MODULE'] != "olaf.settings.dev":
            raise CommandError('This command can only be run in the development environment')

        for i in range(0, options['num_users']):
            UserFactory.create()

