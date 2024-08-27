from django.urls import path, include
from .views import MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("archive", MovieViewSet, basename="movies_viewset")

urlpatterns = [
    path("", include(router.urls))
]