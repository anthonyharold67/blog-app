import profile
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(blank=True,max_length=300)
    bio = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return self.user.username