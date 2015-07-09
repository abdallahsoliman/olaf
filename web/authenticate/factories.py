import factory
from faker import Faker
from . import models

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = factory.PostGenerationMethodCall('set_password','password123')
