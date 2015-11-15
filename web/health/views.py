from django.shortcuts import render
from django.views.generic import ListView
from health.models import HeartRate
from health.serializers import HeartRateSerializer

class HeartRateView(ListView):
    context_object_name = "heart_rates"
    template_name="health/heart_rate.html"

    def get_queryset(self):
        return [HeartRateSerializer(instance=heart_rate).serialize() for heart_rate in HeartRate.objects.all()]

