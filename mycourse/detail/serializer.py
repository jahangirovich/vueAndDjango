from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password','id')

class My(serializers.ModelSerializer):

    class Meta:
        model = my
        fields = ('title','text','user','image','id','username')

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profiles
        fields = "__all__"

class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Add
        fields = "__all__"

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Test
        fields = "__all__"

class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Compare
        fields = "__all__"