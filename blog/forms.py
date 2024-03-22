from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')
