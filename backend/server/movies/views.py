from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        # Customize the response
        if response.status_code == status.HTTP_201_CREATED:
            response.data = {
                "success": True,
                "message": 'Movie created successfully',
                "data": response.data
            }
        else:
            response.data = {
                "success": True,
                "message": "There was an error creating the movie",
                "data": response.data
            }
        
        return response
    