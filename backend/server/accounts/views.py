from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from django.contrib.auth import get_user_model
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer

User = get_user_model()

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response = {
                "success": True,
                "message": "User and Profile created successfully",
                "data": serializer.data
            }
            
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        response = {
            "sucess": False,
            "message": "There was an error in creating User and Profile",
            "data": serializer.errors
        }
        
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)