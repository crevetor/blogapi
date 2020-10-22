from rest_framework import serializers
from django.contrib.auth.models import User

from blogapi.blog.models import Tag, Post, Author

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Author
        fields = ('user', 'photo')
        depth = 1

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'
        depth = 2
