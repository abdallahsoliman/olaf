from django.conf.urls import url
from dorm.views import *

urlpatterns = [
        url(r'$', DormView.as_view()),
        url(r'actuators/', ActuatorView.as_view()),

]
