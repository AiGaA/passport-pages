from django.forms import ModelForm
from django import forms
from .models import Post


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
