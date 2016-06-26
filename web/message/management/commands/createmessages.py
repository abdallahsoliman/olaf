import random
from os import environ
from django.core.management.base import BaseCommand, CommandError
from sms.factories import MessageFactory
from authenticate.models import User
from sms.models import Contact

class Command(BaseCommand):
    help = "creates random number of messages for all contacts associated with a user"

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help="user id to add messages to")

    def handle(self, *args, **options):

        if environ['DJANGO_SETTINGS_MODULE'] != "olaf.settings.dev":
            raise CommandError('This command can only be run in the development environment')

        user = User.objects.get(id=options['user_id'])
        phone_numbers = PhoneNumber.objects.filter(contact__user=user)

        # messages sent by the contacts of our user
        for phone_number in phone_numbers:
            MessageFactory.create_batch(random.randint(5, 25), sender=phone_number, user=user)

        print("Created messages for all contacts of user %d" % options['user_id'])
