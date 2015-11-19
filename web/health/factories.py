from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyInteger, _random
from factory import LazyAttribute
from . import models

class FuzzyHeartRate(FuzzyInteger):

    def __init__(self, base_rate):
        self.base_rate = base_rate

    def fuzz(self):
        fluctuation = _random.randint(1, 10)
        return self.base_rate + fluctuation


class HeartRateFactory(DjangoModelFactory):
    class Meta:
        model = models.HeartRate
        exclude = ('base_rate',)

    base_rate = 50
    value = LazyAttribute(lambda object: FuzzyHeartRate(object.base_rate).fuzz())
