from django.shortcuts import render, get_object_or_404 , redirect, reverse
from django.views import generic, View
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
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
    # comment_form = CommentsForm()
    
    # if request.method == 'POST':
    #     comment_form = CommentsForm(request.POST)
    #     if comment_form.is_valid():
    #         comment = comment_form.save(commit=False)
    #         comment.user = request.user
    #         comment.post = post
    #         comment.save()
    #         return redirect('post_detail', pk=post.id)

    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})


def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    submitted = False
    form = CommentsForm()

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect(reverse('all_posts'))
        else:
            form = CommentsForm()
            if 'submitted' in request.GET:
                submitted = True
    return render(request, "blog/add_comment.html",
                  {'form': form, 'post': post})


def add_post(request):
    submitted = False
    # create a form instance and populate it with data from the request:
    form = AddPost(request.POST, request.FILES)
    # if this is a POST request we need to process the form data
    if request.method == "POST":

        # check whether it's valid:
        if form.is_valid():
            user = form.save(commit=False)
            user.author = User.objects.get(id=request.user.id)
            # process the data in form.cleaned_data as required
            user.save()
            # redirect to a new URL:
            return redirect(reverse('all_posts'))

        # if a GET (or any other method) we'll create a blank form
    else:
        form = AddPost()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "blog/add_post.html",
                  {'form': form, 'submitted': submitted})


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        form = AddPost(request.POST, request.FILES, instance=post)
        # check whether it's valid:
        if form.is_valid():
            user = form.save(commit=False)
            user.author = User.objects.get(id=request.user.id)
            # process the data in form.cleaned_data as required
            user.save()
            # redirect to a new URL:
            return redirect(reverse('all_posts'))

        # if a GET (or any other method) we'll create a blank form
    else:
        form = AddPost(instance=post)
        if 'submitted' in request.GET:
            submitted = True
    return render(request, "blog/edit_post.html", {'form': form, 'post': post})


def delete_post(request, pk):
    """
    TODO:Need to add validations if user is allowed to do this action
    """

    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect(reverse('all_posts'))

