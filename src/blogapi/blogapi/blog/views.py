from rest_framework import viewsets
from django.contrib.auth.models import User

from blogapi.blog.models import Post, Tag
from blogapi.blog.serializers import (
    PostSerializer,
    TagSerializer,
    UserSerializer,
)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-published_date')
    serializer_class = PostSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
