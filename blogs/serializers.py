from .models import *
from userapp.models import BlogUsers
from rest_framework import serializers

class UserDataSerializer(serializers.ModelSerializer):
  class Meta:
    model=BlogUsers
    fields='__all__'


class BlogDataSerializer(serializers.ModelSerializer):
  class Meta:
    model=BlogData
    fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'