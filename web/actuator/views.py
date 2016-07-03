from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from actuator.models import *

class ActuatorView(TemplateView):
    template_name = "actuator/index.html"

