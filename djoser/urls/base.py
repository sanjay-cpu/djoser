from django.conf.urls import url, include
from django.contrib.auth import get_user_model

from djoser import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)

User = get_user_model()

urlpatterns = [
    url(r'^', include(router.urls)),
]
