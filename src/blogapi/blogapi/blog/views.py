from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from blogapi.blog.models import Post, Tag
from blogapi.blog.serializers import (
    PostSummarySerializer,
    PostSerializer,
    TagSerializer,
)

class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all().filter(state='P').order_by('-published_date')
    serializer_class = PostSummarySerializer

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = PostSerializer(instance, context=self.get_serializer_context())
        return Response(serializer.data)

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
