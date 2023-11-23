from rest_framework import serializers
from .models import BlogUsers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogUsers
        fields = ('username', 'email', 'password')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        fields=("email","password")