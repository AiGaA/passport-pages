from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Comment

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        test_user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a test post
        cls.test_post = Post.objects.create(
            author=test_user,
            title='Test Post',
            content='Test content for the post.',
            image='placeholder',
            excerpt='Test excerpt'
        )

    def test_post_author_label(self):
        post = Post.objects.get(pk=self.test_post.pk)
        field_label = post._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_post_title_max_length(self):
        post = Post.objects.get(pk=self.test_post.pk)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_post_content_label(self):
        post = Post.objects.get(pk=self.test_post.pk)
        field_label = post._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_post_created_on_label(self):
        post = Post.objects.get(pk=self.test_post.pk)
        field_label = post._meta.get_field('created_on').verbose_name
        self.assertEqual(field_label, 'created on')

    def test_post_image_label(self):
        post = Post.objects.get(pk=self.test_post.pk)
        field_label = post._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_post_excerpt_label(self):
        post = Post.objects.get(pk=self.test_post.pk)
        field_label = post._meta.get_field('excerpt').verbose_name
        self.assertEqual(field_label, 'excerpt')

    def test_ordering(self):
        ordering = Post._meta.ordering
        self.assertEqual(ordering, ['-created_on'])

    def test_str_representation(self):
        post = Post.objects.get(pk=self.test_post.pk)
        self.assertEqual(str(post), 'Test Post')



class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        test_user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test post
        test_post = Post.objects.create(
            author=test_user,
            title='Test Post',
            content='Test content for the post.',
            image='placeholder',
            excerpt='Test excerpt'
        )

        # Create a test comment
        cls.test_comment = Comment.objects.create(
            post=test_post,
            author=test_user,
            text='Test comment text.',
            approved_comment=True
        )

    def test_comment_post_label(self):
        comment = Comment.objects.get(pk=self.test_comment.pk)
        field_label = comment._meta.get_field('post').verbose_name
        self.assertEqual(field_label, 'post')

    def test_comment_author_label(self):
        comment = Comment.objects.get(pk=self.test_comment.pk)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_comment_text_max_length(self):
        comment = Comment.objects.get(pk=self.test_comment.pk)
        max_length = comment._meta.get_field('text').max_length
        self.assertEqual(max_length, 500)

    def test_comment_created_on_label(self):
        comment = Comment.objects.get(pk=self.test_comment.pk)
        field_label = comment._meta.get_field('created_on').verbose_name
        self.assertEqual(field_label, 'created on')

    def test_comment_approved_comment_label(self):
        comment = Comment.objects.get(pk=self.test_comment.pk)
        field_label = comment._meta.get_field('approved_comment').verbose_name
        self.assertEqual(field_label, 'approved comment')

    def test_ordering(self):
        ordering = Comment._meta.ordering
        self.assertEqual(ordering, ['created_on'])

    def test_str_representation(self):
        comment = Comment.objects.get(pk=self.test_comment.pk)
        self.assertEqual(str(comment), 'Test comment text.')
