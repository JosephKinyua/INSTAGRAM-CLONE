from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    profilePic = models.ImageField(upload_to='profileimages/', null=True, blank=True, default='profileimages/test.png')
    fullName= models.CharField(max_length=255, null=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = HTMLField(null=True, blank=True)

class Post(models.Model):
    picture = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=3000)
    uploadedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)
    
class Comments(models.Model):