from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, login
from .serializers import UserSerializer, LoginSerializer
from .permissions import IsOwner

User = get_user_model()

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == "create":
            # Allow any user to create a profile
            return [AllowAny()]
        else:
            # Require authentication for other actions
            return [IsAuthenticated(), IsOwner()]

    
    def get_object(self):
        obj = super().get_object()
        return obj
    
    def create(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
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
    
class LoginView(APIView):
    permission_classes = [AllowAny] 
    
    def post(self, request: Request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            token = Token.objects.get(user=user)
        
            response = {
                "success": True,
                "message": "Login successful",
                "data": {
                    "token": token.key
                }
            }
            
            # login(request, user)
        
            return Response(data=response, status=status.HTTP_200_OK)

        response = {
            "success": False,
            "message": "Invalid username or password",
            "data": serializer.errors
        }
        
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
            
        