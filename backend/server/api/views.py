from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(http_method_names=["GET", "POST"])
def homepage(request: Request):
    res = {"message": "Hi"}
    return Response(data=res, status=status.HTTP_200_OK)