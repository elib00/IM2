from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import User, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id","first_name", "last_name", "age", "gender", "birthdate"]
    

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    
    email = serializers.CharField(max_length=254)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = User
        fields = ["email", "password", "username", "profile"]
    
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
        
        #create the profile of the user
        Profile.objects.create(user=user, **profile_data)
        return user