from django.shortcuts import render
from django.views import View

# Create your views here.


def home(request):
    return render(request, 'blog/index.html')


# def my_stories(request):
#     return render(request, 'blog/user_stories.html')


def add_post(request):
    return render(request, 'blog/add_post.html')