from django.db import models

class ActuatorType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    command_on = models.CharField(max_length=255)
    command_off = models.CharField(max_length=255)
    on_state_name = models.CharField(max_length=50)
    off_state_name = models.CharField(max_length=50)

class Actuator(models.Model):
    name = models.CharField(max_length=255, unique=True)
    state = models.BooleanField(default=False)
    type = models.ForeignKey(ActuatorType)
