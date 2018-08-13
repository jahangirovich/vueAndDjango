from django.shortcuts import render
from .serializer import *
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authentication import *
from .models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class Migrate(viewsets.ModelViewSet):
  authentication_classes = [TokenAuthentication]
  queryset = my.objects.all()
  serializer_class = My

class Tokens(viewsets.ModelViewSet):
  queryset = Token.objects.all()
  serializer_class = TokenSerializer

class Comments(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer

class Prof(viewsets.ModelViewSet):
  queryset = Profiles.objects.all()
  serializer_class = ProfileSerializer

class Friends(viewsets.ModelViewSet):
  queryset = Add.objects.all()
  serializer_class = FriendSerializer

class Test(viewsets.ModelViewSet):
  queryset = Test.objects.all()
  serializer_class = TestSerializer

class List(viewsets.ModelViewSet):
  queryset = Compare.objects.all()
  serializer_class = ListSerializer