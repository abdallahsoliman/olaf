from django.core.management.base import BaseCommand, CommandError
from health.factories import HeartRateFactory
from random import randint
from time import sleep
from os import environ

class Command(BaseCommand):
    help = 'simulates heart rate monitor data feed'

    def handle(self, *args, **options):

        if environ['DJANGO_SETTINGS_MODULE'] != "olaf.settings.dev":
            raise CommandError('This command can only be run in the development environment')

        base_rate = randint(40, 80)
        print "Started Heart Rate Simulator..."
        while True:
            try:
                hr = HeartRateFactory.create(base_rate=base_rate)
                print hr.value
                sleep(1)
            except KeyboardInterrupt:
                print "Exiting Heart Rate Simulator"
                break
