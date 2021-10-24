from .models import Review, Profile, Post
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        template_name = "add.html"

        fields = "__all__"
        
# exclude = ['user', 'profile', 'date']


# class UpdateUserForm(forms.ModelForm):
#     email = forms.EmailField(max_length=254, help_text='Required.')

#     class Meta:
#         model = Profile
#         fields = ('username', 'email')


# class UpdateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['contact','profile_pic', 'bio']
