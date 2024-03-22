from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the posts
        context = Post.objects.all()
        for post in context:
            comments = Comment.objects.filter(post=post)
            context["count"] = comments.count()
        return context


@login_required
def delete_post(request, _id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=_id)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request, 'The post has been deleted successfully.')
        return redirect('posts')


@login_required
def edit_post(request, _id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=_id)

    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': _id}
        return render(request, 'blog/post_form.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'blog/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})


def home(request):
    posts = Post.objects.all()
    extra_detail = list()
    post_comment_dict = dict()
    for post in posts:
        comments = Comment.objects.filter(post=post)
        count = comments.count()
        post_comment_dict["comment"] = {"count": count}
        post_comment_dict["post"] = post
        extra_detail.append(post_comment_dict.copy())
    context = {
        'posts': extra_detail,
    }
    return render(request, 'blog/home.html', context)


def show_post(request, _id):
    post = Post.objects.get(id=_id)
    comments = Comment.objects.filter(post=post)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post and user to the comment
            new_comment.post = post
            new_comment.author = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'count': comments.count(),
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post.html', context)
