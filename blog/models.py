from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_post")
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    excerpt = models.TextField(blank=True)

    class Meta:
        orderin = ['-created_on']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()
    