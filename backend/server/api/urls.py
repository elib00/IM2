from . import views
from django.urls import path 

urlpatterns = [
    path("", views.homepage, name="api_home"),
    path("get_users/", views.get_users, name="get_users"), 
    path("create_user/", views.create_user, name="create_user")
]
