from rest_framework import serializers
from .models import Cinema, Ticket, ScheduledMovie
from accounts.models import Profile
from movies.models import Movie
from accounts.serializers import ProfileSerializer
from movies.serializers import MovieSerializer


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
        
    def to_representation(self, instance):
        #Override to use nested serializers for output.
        representation = super().to_representation(instance)
        representation["cinema"] = CinemaSerializer(instance.cinema).data
        representation["movie"] = MovieSerializer(instance.movie).data
        return representation
        
class TicketSerializer(serializers.ModelSerializer):
    profile = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all())
    scheduled_movie = serializers.PrimaryKeyRelatedField(queryset=ScheduledMovie.objects.all())

    class Meta:
        model = Ticket
        fields = "__all__"
        
    def to_representation(self, instance):
        #Override to use nested serializers for output.
        representation = super().to_representation(instance)
        representation["profile"] = ProfileSerializer(instance.profile).data
        representation["scheduled_movie"] = ScheduledMovieSerializer(instance.scheduled_movie).data
        return representation