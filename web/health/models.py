from django.db import models
from swampdragon.models import SelfPublishModel
from health.serializers import HeartRateSerializer

class HeartRate(SelfPublishModel, models.Model):
    serializer_class = HeartRateSerializer
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
