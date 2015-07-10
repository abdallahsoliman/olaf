import factory
from faker import Faker
from . import models

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    first_name = factory.LazyAttribute(lambda n: fake.first_name())
    last_name = factory.LazyAttribute(lambda n: fake.last_name())
    email = factory.LazyAttribute(lambda n: fake.email())
    password = factory.PostGenerationMethodCall('set_password','password123')
