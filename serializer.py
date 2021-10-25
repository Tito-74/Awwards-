from rest_framework import serializers
from .models import Profile,Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']
    
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        fields = ['id','user', 'profile_pict', 'bio', 'name','phone','country']

class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'project_image', 'desc', 'url_link','pub_date']