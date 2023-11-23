from django.db import models
from userapp.models import BlogUsers

class BlogData(models.Model):
  user=models.ForeignKey(BlogUsers,on_delete=models.CASCADE)
  image=models.ImageField(upload_to="images_post",null=True,blank=True)
  heading=models.CharField(max_length=100,null=True)
  description=models.TextField(blank=True)
  added_date=models.DateField(auto_now=True)
  like_count = models.IntegerField(default=0)
  comment_count = models.IntegerField(default=0)
  attachment = models.FileField(upload_to='blog_attachments/', null=True, blank=True)

  def __str__(self):
    return self.heading
  
class Comments(models.Model):
  user = models.ForeignKey(BlogUsers,on_delete=models.CASCADE)
  blog=models.ForeignKey(BlogData,on_delete=models.CASCADE)
  text = models.TextField()
  added_date=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user} commented on {self.blog}"

  
class Like(models.Model):
  user = models.ForeignKey(BlogUsers,on_delete=models.CASCADE)
  blog=models.ForeignKey(BlogData,on_delete=models.CASCADE)
  liked=models.BooleanField(default=False)

  class Meta:
      unique_together=["blog","user"]

  def __str__(self) -> str:
      return f"{self.user} liked on {self.blog}"
