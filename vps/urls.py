from django.urls import include, path
from rest_framework.routers import DefaultRouter

from vps.views import VPSViewSet

router = DefaultRouter()
router.register(r"vps", VPSViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
