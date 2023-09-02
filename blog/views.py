from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post

# Create your views here.


class HomePage(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog/index.html'


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog/all_posts.html'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


def add_post(request):
    return render(request, 'blog/add_post.html')
