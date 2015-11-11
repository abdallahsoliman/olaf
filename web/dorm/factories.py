import factory
from factory.fuzzy import _random as random
from faker import Faker
from . import models

fake = Faker()

class FuzzyBoolean(factory.fuzzy.BaseFuzzyAttribute):
    def fuzz(self):
        return random.choice([True, False])

class FuzzyActuatorType(factory.fuzzy.BaseFuzzyAttribute):
    def fuzz(self):
        actuator_types = models.ActuatorType.objects.all()
        if not actuator_types:
            raise Exception("Fuzzy ActuatorType Failed: No actuator types exist")
        return random.choice(actuator_types)

class Lamp(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ActuatorType

    name = "Lamp"
    command_on = "sudo on"
    command_off = "sudo off"
    on_state_name = "on"
    off_state_name = "off"
    on_state_icon = "sun-o"
    off_state_icon = "moon-o"


class Lock(factory.django.DjangoModelFactory):
    class Meta:
        model = models.ActuatorType

    name = "Lock"
    command_on = "sudo lock"
    command_off = "sudo unlock"
    on_state_name = "unlocked"
    off_state_name = "locked"
    on_state_icon = "unlock"
    off_state_icon = "lock"

class ActuatorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Actuator

    name = factory.Sequence(lambda n: "Device #%s" % (n))
    state = FuzzyBoolean().fuzz()

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        if models.ActuatorType.objects.all().count() == 0:
            Lamp.create()
            Lock.create()
        manager = cls._get_manager(model_class)
        kwargs['type'] = FuzzyActuatorType().fuzz()
        return manager.create(*args, **kwargs)

