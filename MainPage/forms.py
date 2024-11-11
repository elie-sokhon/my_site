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


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels = {
            "user_name":"Username",
            "email_address": "Email",
            "password1": "Password",
            "password2": "Confirm your password",
        }