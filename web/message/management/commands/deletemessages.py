from os import environ
from django.core.management.base import BaseCommand, CommandError
from sms.models import Message

class Command(BaseCommand):
    help = "Deletes all messages in database"

    def handle(self, *args, **options):

        if environ['DJANGO_SETTINGS_MODULE'] != "olaf.settings.dev":
            raise CommandError('This command can only be run in the development environment')

        Message.objects.all().delete()
        print("All message objects successfully deleted")
