from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    profilePic = models.ImageField(upload_to='profileimages/', null=True, blank=True, default='profileimages/test.png')
    fullName= models.CharField(max_length=255, null=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = HTMLField(null=True, blank=True)

    def __str__(self):
        return self.username

class Post(models.Model):
    picture = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=3000)
    uploadedBy = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    posted = models.DateTimeField(auto_now_add=True)

class Comments(models.Model):
    comment = models.CharField(max_length=200, null=True, blank=True)
    pic = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

class Likes(models.Model):
    likes = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.likes