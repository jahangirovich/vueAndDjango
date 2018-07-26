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
  permission_classes = [IsAuthenticated]

class Migrate(viewsets.ModelViewSet):
  authentication_classes = [TokenAuthentication]
  queryset = my.objects.all()
  serializer_class = My

class Tokens(viewsets.ModelViewSet):
  queryset = Token.objects.all()
  serializer_class = TokenSerializer
