from django.db import models

class HeartRate(models.Model):
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
