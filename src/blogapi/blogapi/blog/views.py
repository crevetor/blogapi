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

    def list(self, request):
        serializer = PostSummarySerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        post = get_object_or_404(self.queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
