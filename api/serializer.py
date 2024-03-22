from rest_framework import serializers
from blog.models import Post


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'published_at', 'author', 'category']


class TitleBlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title',]
