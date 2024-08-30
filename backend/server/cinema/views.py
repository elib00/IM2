from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .models import ScheduledMovie, Cinema
from .serializers import ScheduledMovieSerializer, CinemaSerializer

class ScheduledMovieViewSet(viewsets.ModelViewSet):
    queryset = ScheduledMovie.objects.all()
    serializer_class = ScheduledMovieSerializer
    permission_classes = [IsAuthenticated]
    
class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    permission_classes = [IsAuthenticated]    