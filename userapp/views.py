from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListAPIView ,CreateAPIView
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password
# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        print("inside the serializer")
        
            
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['user_id'] = user.id
        token['is_superuser'] = user.is_superuser
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserRegister(CreateAPIView):
    queryset=BlogUsers.objects.all()
    serializer_class=UserSerializer

    def get (self,request,*args,**kwargs):
        return render(request,'user/register.html')
    def post(self, request, *args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            if request.data['password']==request.data['password2']:
                password = make_password(request.data.get('password'))
                serializer.save(password=password) 

                return render(request,'user/login.html')
            else:
                error_messages = {'password': ['Passwords do not match.']}
                return render(request, 'user/register.html', {'errors': error_messages})
        else:
            error_messages = serializer.errors
            return render(request, 'user/register.html', {'errors': error_messages})