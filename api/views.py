from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BlogPostSerializer, TitleBlogPostSerializer
from blog.models import Post
from django_filters.rest_framework import DjangoFilterBackend


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'author']


class TitleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = TitleBlogPostSerializer
