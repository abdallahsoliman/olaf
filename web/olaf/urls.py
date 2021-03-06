from django.conf.urls import include, url

urlpatterns = [
        url(r'^api', include('api.urls')),
        url(r'^authenticate', include('authenticate.urls')),
        url(r'^actuator', include('actuator.urls')),
        url(r'^health', include('health.urls')),
        url(r'^message', include('message.urls')),
]
