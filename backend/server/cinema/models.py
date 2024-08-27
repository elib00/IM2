from django.db import models
from accounts.models import Profile
from movies.models import Movie

class Cinema(models.Model):
    capacity = models.PositiveIntegerField(default=0)
    cinema_number = models.PositiveIntegerField()
    
class Ticket(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="profile_tickets")
    scheduled_movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="movie_tickets")
    is_active = models.BooleanField(default=True)
    
class ScheduledMovie(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name="cinema_scheduled_movies")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="scheduled_movies")
    audience_number = models.PositiveIntegerField(default=0)
    
    
    
    
