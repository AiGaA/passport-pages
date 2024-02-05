from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages import get_messages
from django.contrib import messages
from blog.models import Post, Comment
from blog.forms import AddPost, CommentsForm

# Create your tests here.

class TestPostView(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword',
            email="test@test.com"
        )
        self.post = Post(
            title="Blog title", 
            author=self.user,
            excerpt="Blog excerpt",
            content="Blog content")
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'post_detail', args=[str(self.post.pk)]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertQuerysetEqual(
            response.context['comments'], Comment.objects.filter(post=self.post), transform=lambda x: x)


class TestAddCommentView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword',
            email="test@test.com"
        )
        self.post = Post.objects.create(
            title="Blog title", 
            author=self.user,
            excerpt="Blog excerpt",
            content="Blog content"
        )
        self.url = reverse('add_comment', args=[str(self.post.pk)])

    def test_add_comment_view_get_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_comment.html')
        self.assertIsInstance(response.context['form'], CommentsForm)
        self.assertEqual(response.context['post'], self.post)

    def test_add_comment_view_get_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)  
        # Redirect to login page
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

    def test_add_comment_view_post_valid(self):
        self.client.force_login(self.user)
        data = {'text': 'Test comment'}
        response = self.client.post(self.url, data, follow=True)

        # Check that the comment was created
        self.assertEqual(Comment.objects.count(), 1)
        comment = Comment.objects.first()
        self.assertEqual(comment.author, self.user)
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.text, 'Test comment') 

        # Check for the success message
        self.assertContains(response, 'Comment added successfully', status_code=200) 
      