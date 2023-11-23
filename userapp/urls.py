from django.urls import path
from .views import *
# from . import views

urlpatterns = [
   path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('register/',UserRegister.as_view(),name='register'),
   path('dashboard/',dashboard, name='dashboard'),
   path('reg/',RegisterView, name='reg'),
   path('',LoginView, name='login'),
   path('adminblog/',AdminBlog, name='adminblog'),
   path('userlist/', ListUserView.as_view(), name='userlist'),
   path('userlist/<int:userId>/', ListUserView.as_view(), name='userlist')
]
