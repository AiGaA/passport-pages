from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import AddPost


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


# def add_post(request):
#     return render(request, 'blog/add_post.html')


def add_post(request):
    submitted = False
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AddPost(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("blog/all_posts.html?submitted=True")

        # if a GET (or any other method) we'll create a blank form
        else:
            form = AddPost()
            if 'submitted' in request.GET:
                submitted = True

    return render(request, "blog/add_post.html", {'form': form, 'submitted': submitted})
