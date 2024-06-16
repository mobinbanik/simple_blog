from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.html import mark_safe


UserModel = get_user_model()


def get_user_path(instance, file_name):
    return "media/users/{0}/{1}/{2}/{3}/{4}".format(
        instance.date_joined.year,
        instance.date_joined.month,
        instance.date_joined.day,
        instance.username,
        file_name,
    )


def get_post_path(instance, file_name):
    return "media/posts/{0}/{1}/{2}/{3}/{4}".format(
        instance.published_at.year,
        instance.published_at.month,
        instance.published_at.day,
        instance.slug,
        file_name,
    )


def get_post_path_for_images(instance, file_name):
    return "media/posts/{0}/{1}/{2}/{3}/{4}".format(
        instance.post.published_at.year,
        instance.post.published_at.month,
        instance.post.published_at.day,
        instance.post.slug,
        file_name,
    )


class User(UserModel):
    profile_image = models.ImageField(
        upload_to=get_user_path,
        null=True,
        blank=True,
    )

    def img_preview(self):
        try:
            return mark_safe(f'<img src = "{self.profile_image.url}" style="max-width:200px; max-height:200px"/>')
        except Exception as e:
            return e.__str__()

    def __str__(self):
        return self.username


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


class Tag(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    slug = models.SlugField(
        unique=True,
    )
    title = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        verbose_name='title',
    )
    content = models.TextField()
    published_at = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(upload_to=get_post_path, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False)
    active = models.BooleanField(
        default=True
    )
    # simple:0, vertical:1, gallery:2, slider:3
    type = models.IntegerField(default=0)

    tags = models.ManyToManyField(
        "Tag",
        blank=True,
        related_name='posts',
    )

    def img_preview(self):
        try:
            return mark_safe(f'<img src = "{self.thumbnail.url }" style="max-width:200px; max-height:200px"/>')
        except Exception as e:
            return e.__str__()

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
        default=False,
    )
    is_reply = models.BooleanField(default=False)
    parent = models.ForeignKey(
        "Comment",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="reply",
    )

    def __str__(self):
        return f"comment <{self.author.username}>"

    class Meta:
        ordering = ['-pub_date']
        verbose_name = "comment"
        verbose_name_plural = "comments"


class ImageFile(models.Model):
    image = models.ImageField(upload_to=get_post_path_for_images)
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        related_name="images_post",
        null=False,
        blank=False,
    )
    alt_text = models.CharField(max_length=125)

    def img_preview(self):
        try:
            return mark_safe(f'<img src = "{self.image.url}" style="max-width:200px; max-height:200px"/>')
        except Exception as e:
            return e.__str__()

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = 'Image File'
        verbose_name_plural = 'Image Files'
