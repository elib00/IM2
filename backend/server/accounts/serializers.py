from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model, authenticate
from .models import Profile

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "age", "gender", "birthdate"]
    

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    email = serializers.CharField(max_length=254)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, max_length=100, write_only=True)
    
    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "profile"]
    
    def validate(self, attrs):
        email_exists = User.objects.filter(email=attrs["email"]).exists()
        if email_exists:
            raise ValidationError("Email is already in use")
        
        username_exists = User.objects.filter(email=attrs["username"]).exists()
        if username_exists:
            raise ValidationError("Username is already in use")
        
        return super().validate(attrs)

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        password = validated_data.pop("password")
        
        user = super().create(validated_data) #create the user instance without the password
        user.set_password(password)
        user.save()
        
        #create token
        Token.objects.create(user=user)
        
        #create the profile of the user
        Profile.objects.create(user=user, **profile_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(min_length=8, max_length=100, write_only=True)
    
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        
        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise ValidationError("Invalid credentials, please try again")
            if not user.is_active:
                raise ValidationError("This account is inactive")
            
            attrs["user"] = user
        else:
            raise ValidationError("Both email and password must be provided")
        
        return super().validate(attrs)
    