from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','first_name', 'email', 'profile_img', 'is_active', 'is_verified', 'phone_number', 'roles']
