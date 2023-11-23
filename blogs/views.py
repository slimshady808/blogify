from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import UpdateAPIView,ListAPIView,CreateAPIView,DestroyAPIView,ListCreateAPIView
from rest_framework.response import Response
from django.shortcuts import render, redirect,get_object_or_404
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
# Create your views here.




class AddBlogs(CreateAPIView):
    queryset=BlogData.objects.all()
    serializer_class=AddBlogSerializer
    template_name = 'users/admin-add-blog.html'

    def post(self,request,*args,**kwargs):
      user_id=request.data.get('user_id')

      try:
           user=BlogUsers.objects.get(id=user_id)
           image=request.data.get('image')
           title=request.data.get('title')
           description = request.data.get('description')
           attachments = request.data.get("attachments")

           if user and image and title and description:
                blog=BlogData.objects.create(
                     description=description,
                     title=title,
                     user=user,
                     attachments=attachments
                )
           else:
                return Response({'message': 'Missing required data'})
      except BlogUsers.DoesNotExist:
            return Response({'message': 'User not found'})
      
def DeleteBlog(request, blogId):
    blog = get_object_or_404(BlogData, id=blogId)
    print(blog,"blogsddddd")
    blog.delete()
    return redirect('adminblog')

def UserHome(request):
        context = {
             'blogs': BlogData.objects.all()
        }
   
        return render(request, 'user/user-blog-list.html' , context)

class UpdateBlogPost(APIView):
    def get(self,request,id):
          try:
               blog=BlogData.objects.get(id=id)

               context={'blog_data':blog}
               return render (request,'user/admin-blog-edit',context)
          except BlogData.DoesNotExist:
               raise Http404
    def post(self,request,id):
         blog=BlogData.objects.get(id=id)

         serializer=BlogDataSerializer(blog,data=request.data,partial=True)
         if serializer.is_valid():
              serializer.save()
              return redirect(reverse('adminblog'))
         else:
            context = {'blog_data': blog, 'errors': serializer.errors}
            return render(request, 'users/admin-edit-blog.html', context)

def add_blog(request):
     return render(request,'users/admin-add-blog.html')

@api_view(['POST'])
def add_comment(request):
     user_id=request.data.get('userid')
     post_id=request.data.get('comment')
     comment_text = request.data.get('comment')
     serializer= CommentSerializer(data={
          'user':user_id,
          'post':post_id,
          'comment':comment_text,
     })

     if serializer.is_valid():
          serializer.save()

          return redirect('home')
     return Response(serializer.errors)

class GetComments(APIView):
     def get(self,request,post_id):
          try:
               blog=get_object_or_404(BlogData,pk=post_id)

               blogs=BlogData.objects.all()

               comments=Comments.objects.filter(post=post_id)

               context={
                    'comments':comments,
                    'blogs':blogs,
                    'error':None,
               }

               return render(request,'users/user-blog-list.html',context)
          except BlogData.DoesNotExist:
               error ="Blog not found"
               context={
                'comments': [],
                'blogs': blogs,  
                'error': error,
               }

               return render(request,'user/user-blog-list.html',context)
          
