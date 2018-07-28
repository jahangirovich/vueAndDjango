from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class my(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    image = models.ImageField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    def __str__(self):
        return "%s"%self.title

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(my,on_delete=models.CASCADE)
    username = models.CharField(max_length=40)
    def __str__(self):
        return "%s"%self.text