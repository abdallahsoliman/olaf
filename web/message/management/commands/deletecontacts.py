from os import environ
from django.core.management.base import BaseCommand, CommandError
from sms.models import Contact, PhoneNumber

class Command(BaseCommand):
    help = "Deletes all phone numbers and contacts. Only for development environment."

    def handle(self, *args, **options):

        if environ['DJANGO_SETTINGS_MODULE'] != "olaf.settings.dev":
            raise CommandError('This command can only be run in the development environment')

        PhoneNumber.objects.all().delete()
        Contact.objects.all().delete()

        print("All contacts deleted.")
