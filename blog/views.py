from django.shortcuts import render, get_object_or_404 , redirect, reverse
from django.views import generic, View
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post, Comment
from .forms import AddPost, CommentsForm


# Create your views here.
class HomePage(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')[:3]
    template_name = 'blog/index.html'


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog/all_posts.html'


class UserPostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog/user_posts.html'


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentsForm()

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment added successfully')
            return redirect('post_detail', pk=post.pk)
    return render(request, "blog/add_comment.html",
                  {'form': form, 'post': post})


@login_required
def add_post(request):
    submitted = False
    form = AddPost(request.POST, request.FILES)

    if request.method == "POST":
        # check whether it's valid:
        if form.is_valid():
            user = form.save(commit=False)
            user.author = User.objects.get(id=request.user.id)
            user.save()
            messages.success(request, 'Post added successfully')
            return redirect(reverse('my_posts'))

    else:
        form = AddPost()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "blog/add_post.html",
                  {'form': form, 'submitted': submitted})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES, instance=post)
        # check whether it's valid:
        if form.is_valid():
            user = form.save(commit=False)
            user.author = User.objects.get(id=request.user.id)
            user.save()
            return redirect(reverse('all_posts'))

    else:
        form = AddPost(instance=post)
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "blog/edit_post.html", {'form': form, 'post': post})


@login_required
def delete_post(request, pk):
    """
    Delete post
    """
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect(reverse('all_posts'))