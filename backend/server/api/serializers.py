from rest_framework import serializers
from .models import User  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id", 
            "firstname", 
            "lastname", 
            "age", 
            "gender", 
            "created_at",
            "updated_at"
        ]
    
      
    
    
    
        
