from django.urls import path, include
from .views import ScheduledMovieViewSet, CinemaViewSet, TicketViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("scheduled_movie", ScheduledMovieViewSet, basename="scheduled_movie_viewset")
router.register("cinema_details", CinemaViewSet, basename="cinema_details_viewset")
router.register("tickets", TicketViewSet, basename="tickets_viewset")

urlpatterns = [
    path("", include(router.urls)),
]