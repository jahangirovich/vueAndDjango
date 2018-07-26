from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class My(serializers.ModelSerializer):

    class Meta:
        model = my
        fields = "__all__"

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = "__all__"