from django.urls import path, include
from rest_framework import routers
from .views import MyUserView

router = routers.DefaultRouter()
router.register('', MyUserView)

urlpatterns = [
    path('',include(router.urls)),
]
