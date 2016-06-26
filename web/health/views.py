from django.shortcuts import render
from django.views.generic import ListView
from health.models import HeartRate

class HeartRateView(ListView):
    context_object_name = "heart_rates"
    template_name="health/heart_rate.html"

    def get_queryset(self):
        return []

    def start_heart_rate_monitor(self):
        pass

    def stop_heart_rate_monitor(self):
        pass

