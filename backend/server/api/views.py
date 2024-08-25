from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, APIView
# from .models import User
# from .serializers import UserSerializer
from django.shortcuts import get_object_or_404 

# class UserOperationsView(APIView):
#     serializer_class = UserSerializer
        
#     #for creating a new user
#     def post(self, request: Request, *args, **kwargs):
#         data = request.data
#         serializer = self.serializer_class(data=data)
#         if serializer.is_valid():
#             serializer.save()
            
#             res = {
#                 "success": True,
#                 "message": "User created successfully",
#                 "data": serializer.data
#             }
            
#             return Response(data=res, status=status.HTTP_201_CREATED)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request: Request, user_id: int, *args, **kwargs):
#         user = get_object_or_404(User, pk=user_id) #get the user or raise if not found
#         serializer = self.serializer_class(instance=user)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def put(self, request: Request, user_id: int, *args, **kwargs):
#         user = get_object_or_404(User, pk=user_id)
#         new_user_data = request.data
#         serializer = self.serializer_class(instance=user, data=new_user_data)
        
#         if serializer.is_valid():
#             serializer.save()
#             res = {
#                 "success": True, 
#                 "message": f"User with id {user_id} updated successfully",
#                 "data": serializer.data
#             }
            
#             return Response(data=res, status=status.HTTP_200_OK)

#         return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
    
#     def delete(self, request: Request, user_id: int, *args, **kwargs):
#         user = get_object_or_404(User, pk=user_id)
#         user.delete()
#         return Response(status=HTTP_204_NO_CONTENT)

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


        