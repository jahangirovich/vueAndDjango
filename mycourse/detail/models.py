from django.db import models

from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class my(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    image = models.ImageField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    def __str__(self):
        return "%s"%self.title


class Profiles(models.Model):
    image = models.ImageField()
    firstName = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    date = models.DateField(default=datetime.now)
    username = models.CharField(max_length=50)
    def __str__(self):
        return "%s"%self.username

class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Profiles,on_delete=models.CASCADE)
    post = models.ForeignKey(my,on_delete=models.CASCADE)
    username = models.CharField(max_length=40)
    userImage = models.TextField()

    def __str__(self):
        return "%s"%self.text

class Add(models.Model):
    username = models.CharField(max_length=50)
    friend = models.ForeignKey(Profiles,on_delete=models.CASCADE)

class Test(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=100)

class Compare(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=100)
    wrong = models.CharField(max_length=100)
    username1 = models.CharField(max_length=100)
    username2 = models.CharField(max_length=100)