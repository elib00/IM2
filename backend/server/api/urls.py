from . import views
from django.urls import path 

urlpatterns = [
    path('users/get_users/', views.get_all_users, name='get_users'), 
    path('users/create_user/', views.UserOperationsView.as_view(), name='create_user'),
    path('users/get_user/<int:user_id>/', views.UserOperationsView.as_view(), name='user_detail'),
    path('users/update_user/<int:user_id>/', views.UserOperationsView.as_view(), name='update_user'),
    path('users/delete_user/<int:user_id>/', views.UserOperationsView.as_view(), name='delete_user'),
]
