from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

@api_view(http_method_names=["GET", "POST"])
def homepage(request: Request):
    res = {"message": "Hi"}
    return Response(data=res, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def get_users(request: Request):
    users = User.objects.all()
    serializer = UserSerializer(instance=users, many=True) #many = true is for serializing a query set
    
    res = {
        "success": True, 
        "message": "Users list successfully retrieved",
        "data": serializer.data
    }
    
    return Response(data=res, status=status.HTTP_200_OK)

@api_view(http_method_names=["POST"])
def create_user(request: Request):
    data = request.data
    serializer = UserSerializer(data=data)
    
    if serializer.is_valid():
        serializer.save()
        
        res = {
            "success": True,
            "message": "User created successfully",
            "data": serializer.data
        }
        
        return Response(data=res, status=status.HTTP_201_CREATED)
    
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    