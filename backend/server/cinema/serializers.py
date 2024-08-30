from rest_framework import serializers
from .models import Cinema, Ticket, ScheduledMovie
from accounts.models import Profile
from accounts.serializers import ProfileSerializer
from movies.serializers import MovieSerializer
from movies.models import Movie

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = "__all__"
        
class ScheduledMovieSerializer(serializers.ModelSerializer):
    cinema = serializers.PrimaryKeyRelatedField(queryset=Cinema.objects.all())
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())

    class Meta:
        model = ScheduledMovie
        fields = "__all__"
        
class TicketSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    scheduled_movie = ScheduledMovieSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = "__all__"