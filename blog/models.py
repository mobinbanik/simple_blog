from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name="category name",
        blank=False,
        null=False,
    )
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        verbose_name='title',
    )
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)
    active = models.BooleanField(
        default=True
    )
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="author",
    )
    text = models.TextField(
        max_length=700,
        verbose_name="text",
        blank=False,
        null=False,
    )
    name = models.CharField(
        max_length=60,
        verbose_name="name",
        blank=False,
        null=False,
    )
    pub_date = models.DateTimeField(
        default=timezone.now,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    # If you want to check comments first set default to False
    active = models.BooleanField(
        default=True,
    )

    def __str__(self):
        return f"comment <{self.author.username}>"

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "comment"
        verbose_name_plural = "comments"
