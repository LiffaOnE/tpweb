from django.urls import path, include
from rest_framework import routers

from api.views import ServiceViewSet

router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet)

urlpatterns = [
    path('', include(router.urls))
]