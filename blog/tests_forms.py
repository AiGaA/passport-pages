from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import AddPost, CommentsForm

# Create your tests here.

# Test Add Comment
class TestAddPostForm(TestCase):

    def test_valid_form(self):
        # Create a path to check the photo passes validation
        image_path = 'static/images/placeholder-img.png'
        files = SimpleUploadedFile(name='placeholder-img.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        form_data = {
            'title': 'Test Title',
            'content': 'Test Content',
            'image': files,
        }

        # Create a form instance with the provided data
        form = AddPost(data=form_data)
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    
    def test_blank_form(self):
        # Create a form instance with no data
        form = AddPost(data={}, files={})

        # Check if the form is not valid
        self.assertFalse(form.is_valid(), msg="Form is valid")


    def test_missing_required_field(self):
        # Create a path to check the photo passes validation
        image_path = 'static/images/placeholder-img.png'
        files = SimpleUploadedFile(name='placeholder-img.png', content=open(image_path, 'rb').read(), content_type='image/jpeg')
        # Create a dictionary with valid data, but omitting the 'title' field
        form_data = {
            'content': 'Test Content',
            'image': files,
        }

        # Create a form instance with the missing 'title' field
        form = AddPost(data=form_data)

        # Check if the form is not valid
        self.assertFalse(form.is_valid(), msg="Form is valid")
        # Check if the 'title' field has a validation error
        self.assertIn('title', form.errors.keys(), msg="Missing required field error not found")


# Test Comment form
class TestCommentForm(TestCase):
    def test_form_is_valid(self):
        comment_form = CommentsForm({'text': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg="Form is valid")

    def test_form_is_invalid(self):
        comment_form = CommentsForm({'text': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")