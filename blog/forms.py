from .models import Post

from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text',]

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Enter Your Offitial Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]        