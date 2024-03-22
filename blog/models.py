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
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']
