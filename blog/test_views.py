from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.contrib.messages import get_messages
from django.contrib import messages
from django.core.files.uploadedfile import SimpleUploadedFile
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


class TestAddPostView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
            email='test@example.com'
        )
    
    def test_add_post_view_get(self):
        # Test GET request to the add_post view
        self.client.force_login(self.user)
        response = self.client.get(reverse('add_post'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_post.html')
        self.assertContains(response, 'Add your story')
        self.assertIsInstance(response.context['form'], AddPost)
        self.assertFalse(response.context['submitted'])


    def test_add_post_view_post_valid(self):

        self.client.login(username='testuser', password='testpassword')
        
        # Create a path to check the photo passes validation
        image_path = 'static/images/placeholder-img.png'
        files = SimpleUploadedFile(name='placeholder-img.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')

        # Send a POST request with valid data to the view
        response = self.client.post(reverse('add_post'), data={
            'title': 'Test Title',
            'content': 'Test Content',
            'image': files,
        })

        # Check that the response has a 302 status code (redirect after successful form submission)
        self.assertEqual(response.status_code, 302)

        # Follow the redirect to check the content on the redirected page
        redirect_url = response.url
        redirected_response = self.client.get(redirect_url)
        self.assertContains(redirected_response, 'Post added successfully')


    def test_add_post_view_post_invalid(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('add_post'), data={})

        # Check that the response has a 200 status code
        self.assertEqual(response.status_code, 200)

        # Check that the error message 'This field is required.' is present in the response
        self.assertContains(response, 'This field is required.')


    def test_add_post_view_get_with_submitted_param(self):
        # Test GET request to the add_post view with 'submitted' parameter
        self.client.force_login(self.user)
        response = self.client.get(reverse('add_post') + '?submitted=true')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_post.html')
        self.assertIsInstance(response.context['form'], AddPost)
        self.assertTrue(response.context['submitted'])


class TestEditPostView(TestCase):
    def setUp(self):
        # Create a path to check the photo passes validation
        image_path = 'static/images/placeholder-img.png'
        files = SimpleUploadedFile(name='placeholder-img.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')

        # Create a user for authentication
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a post for testing
        self.post = Post.objects.create(
            title='Test Title',
            content='Test Content',
            image=files,
            author=self.user
        )

    def test_edit_post_view_get(self):
        # Login the user
        self.client.login(username='testuser', password='testpassword')

        # Make a GET request to the edit_post view
        response = self.client.get(reverse('edit_post', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Edit your story')

    def test_edit_post_view_post_valid(self):
        self.client.login(username='testuser', password='testpassword')
        
        # Create a path to check the photo passes validation
        image_path = 'static/images/placeholder-img.png'
        files = SimpleUploadedFile(name='placeholder-img.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')

        valid_form_data = {
            'title': 'Updated Title',
            'content': 'Updated Content',
            'image': files,
        }

        response = self.client.post(reverse('edit_post', kwargs={'pk': self.post.pk}), data=valid_form_data)
        self.assertRedirects(response, reverse('my_posts'))

        updated_post = Post.objects.get(pk=self.post.pk)

        self.assertEqual(updated_post.title, 'Updated Title')
        self.assertEqual(updated_post.content, 'Updated Content')


    def test_edit_post_view_post_invalid(self):

        self.client.login(username='testuser', password='testpassword')
        image_path = 'static/images/placeholder-img.png'
        files = SimpleUploadedFile(name='placeholder-img.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')

        invalid_form_data = {
            'title': '',
            'content': 'Updated Content',
            'image': files,
        }

        response = self.client.post(reverse('edit_post', kwargs={'pk': self.post.pk}), data=invalid_form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This field is required.')
        updated_post = Post.objects.get(pk=self.post.pk)

        self.assertEqual(updated_post.title, 'Test Title')
        self.assertEqual(updated_post.content, 'Test Content')


class TestDeletePostView(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a path to check the photo passes validation
        image_path = 'static/images/placeholder-img.png'
        files = SimpleUploadedFile(name='placeholder-img.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')

        # Create a test post
        self.post = Post.objects.create(
            title='Test Title',
            content='Test Content',
            image=files,
            author=self.user,
        )


    def test_delete_post_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(reverse('delete_post', kwargs={'pk': self.post.pk}))

        self.assertRedirects(response, reverse('my_posts'))

        # Check that the post has been deleted from the database
        with self.assertRaises(Post.DoesNotExist):
            deleted_post = Post.objects.get(pk=self.post.pk)

    
    def test_delete_post_view_unauthenticated_user(self):
        self.client.logout()

        response = self.client.post(reverse('delete_post', kwargs={'pk': self.post.pk}))

        self.assertRedirects(response, f'/accounts/login/?next={reverse("delete_post", kwargs={"pk": self.post.pk})}')

        # Check that the post still exists in the database
        existing_post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(existing_post.title, 'Test Title')
        self.assertEqual(existing_post.content, 'Test Content')


    def test_delete_post_view_invalid_post(self):
        self.client.login(username='testuser', password='testpassword')

        # Make a POST request to the delete_post view with an invalid post ID
        response = self.client.post(reverse('delete_post', kwargs={'pk': 999}))

        # Check that the response returns a 404 status code
        self.assertEqual(response.status_code, 404)

        # Check that no post has been deleted from the database
        existing_post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(existing_post.title, 'Test Title')
        self.assertEqual(existing_post.content, 'Test Content')


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
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Comment added successfully') 
    

    def test_add_comment_view_post_unauthenticated(self):
        data = {'text': 'Test comment'}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)  
        # Redirect to login page
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')


    def test_add_comment_view_post_anonymous(self):
        self.client.logout()
        data = {'text': 'Test comment'}
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 302)  
        # Redirect to login page
        self.assertRedirects(response, f'/accounts/login/?next={self.url}')

