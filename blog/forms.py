from django.forms import ModelForm
from django import forms
from .models import Post
from cloudinary.models import CloudinaryField


class AddPost(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
