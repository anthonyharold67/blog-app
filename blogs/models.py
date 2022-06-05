from urllib import request
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image=models.CharField(blank=True,max_length=300)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=(('D', 'Draft'), ('P', 'Published')))
    blog_view = models.PositiveIntegerField(default=0)
    blog_like=models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,null=True,blank=True)
    blog_comment = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:20]

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True,blank=True)
    body = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']


