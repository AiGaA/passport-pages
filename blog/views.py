from django.shortcuts import render
from django.views import generic, View
from .models import Post

# Create your views here.


def home(request):
    return render(request, 'blog/index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_on')
    template_name = 'blog/all_posts.html'


class PostDetailView(View):

    def get(self, request, slug, *args, **kwards):
        post = get_object_or_404(slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )


def add_post(request):
    return render(request, 'blog/add_post.html')