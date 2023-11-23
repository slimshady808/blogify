from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import ListAPIView ,CreateAPIView
from .models import *
from .serializers import *
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from blogs.models import *
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

class ListUserView(ListAPIView):
    http_method_names=['get','delete']
    def get(self,request,*args,**kwargs):
        context={
            'users':BlogUsers.objects.filter(is_superuser=False).order_by('-id')
        }
        return render(request,'user/admin-user-list.html',context)
    def delete(self,request,*args,**kwargs):
        user_id=kwargs.get('user_id')

        try:
            user=BlogUsers.objects.get(id=user_id)

            user.delete
            return Response({'message':'user deleted successfully'},status=204)
        except BlogUsers.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)


def dashboard(request):
        return render(request, 'user/dashboard.html')

def LoginView(request):
        return render(request, 'user/login.html')
def RegisterView(request):
        return render(request, 'user/register.html')

def AdminBlog(request):
     
        context = {
             'blogs': BlogData.objects.all()
        }
        print(context,"got datacxzzx")
        return render(request, 'user/admin-blog.html' , context)