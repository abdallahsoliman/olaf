from django.db import models
from swampdragon.models import SelfPublishModel
from health.serializers import HeartRateSerializer

class HeartRate(models.Model, SelfPublishModel):
    serializer_class = HeartRateSerializer
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
