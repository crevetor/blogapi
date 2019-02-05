from rest_framework import viewsets
from django.contrib.auth.models import User

from blogapi.blog.models import Post, Tag
from blogapi.blog.serializers import (
    PostSerializer,
    TagSerializer,
)

    queryset = Post.objects.all().order_by('-published_date')
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
