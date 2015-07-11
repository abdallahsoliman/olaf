from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api import views

router = routers.DefaultRouter()

# authenticate
router.register(r'users', views.UserViewSet)
# sms
router.register(r'messages', views.MessageViewSet)
router.register(r'contacts', views.ContactViewSet)

urlpatterns = [
    url(r'^auth/token/', obtain_auth_token),
]
urlpatterns += router.urls
