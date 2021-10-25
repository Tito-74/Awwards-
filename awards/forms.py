from .models import Review, Profile, Post
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        template_name = "add.html"

        fields = "__all__"



class RatingsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['design', 'usability', 'creativity', 'comment']
        
