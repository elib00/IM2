from django.urls import path, include
from .views import UserProfileViewSet, LoginView
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
router.register("users", UserProfileViewSet, basename="users_view")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginView.as_view(), name="login_view"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify")
]

