from django.db import models

# class User(models.Model):
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     age = models.PositiveIntegerField(null=False, default=0)
#     gender = models.CharField(max_length=50, default="Other")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
# class Movie(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     actors = models.TextField()
#     director = models.CharField(max_length=100)
#     rating = models.PositiveIntegerField(default=0)     