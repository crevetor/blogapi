from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):

    def __str__(self):
        return self.tag

    tag = models.CharField(max_length=255, unique=True)
    description = models.TextField()

class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')

class Post(models.Model):

    def __str__(self):
        return self.title

    POST_STATES = (
        ('D', 'Draft'),
        ('P', 'Published')
    )

    author = models.ForeignKey(
        Author,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Author of the post'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Associated tags'
    )
    state = models.CharField(max_length=1, choices=POST_STATES)

    title = models.CharField(max_length=255)
    content = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
