import factory
from faker import Faker
from factory.fuzzy import _random as random
from authenticate.models import User
from . import models

fake = Faker()

class PhoneNumberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.PhoneNumber

    contact = factory.LazyAttribute(lambda o: factory.Iterator(models.Contact.objects.all()))
    number = factory.LazyAttribute(lambda o: models.PhoneNumber.format_number("%d" % factory.fuzzy.FuzzyInteger(111111111, 999999999).fuzz()))


class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Contact

    user = factory.LazyAttribute(lambda o: factory.Iterator(User.objects.all()))
    name = factory.LazyAttribute(lambda o: fake.name())


class MessageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Message

    sender = factory.LazyAttribute(lambda o: factory.Iterator(models.Contact.objects.all()))
    user = factory.LazyAttribute(lambda o: factory.Iterator(User.objects.all()))
    content = factory.LazyAttribute(lambda o: fake.paragraph(2))
