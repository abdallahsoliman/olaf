from os import environ
from django.core.management.base import BaseCommand, CommandError
from sms.factories import ContactFactory, PhoneNumberFactory
from authenticate.models import User

class Command(BaseCommand):
    help = "Creates 'x' new contacts for user with specified id. Only for development environment."

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help="user id to add contacts to")
        parser.add_argument('num_contacts', type=int, help="number of contacts to create")

    def handle(self, *args, **options):

        if environ['DJANGO_SETTINGS_MODULE'] != "olaf.settings.dev":
            raise CommandError('This command can only be run in the development environment')

        for i in range(options['num_contacts']):
            user = User.objects.get(id=options['user_id'])
            contact = ContactFactory.create(user=user)
            PhoneNumberFactory.create(contact=contact)

        print("Created %d contacts for user with id %d" % (options['num_contacts'], options['user_id']))
