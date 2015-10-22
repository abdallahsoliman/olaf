from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from dorm.models import Actuator

class ActuatorView(ListView):
    template_name="dorm/actuator_list.html"

    def get_queryset(self):
        return Actuator.objects.all()

class DormView(TemplateView):
    template_name = "dorm/index.html"

