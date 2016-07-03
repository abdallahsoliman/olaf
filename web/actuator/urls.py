from django.conf.urls import url
from actuator.views import *

urlpatterns = [
    url('^$', ActuatorView.as_view(), name="actuator"),        
]
