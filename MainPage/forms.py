from django import forms
from .models import Comment, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["product"]
        labels = {
            "user_name":"Your Name",
            "email_address": "Your Email",
            "text":"Your Comment",
            "created_at": "Created at:",
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email Address")
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {
            "username": "Username",
            "password1": "Password",
            "password2": "Confirm Password",
        }

