from django.contrib import admin
from .models import Post, Category, Comment, User, ImageFile, Tag


# Register your models here.
class ImageFileInLine(admin.TabularInline):
    model = ImageFile


class CommentInLine(admin.TabularInline):
    model = Comment

    extra = 0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ImageFile)
class ImageFileAdmin(admin.ModelAdmin):
    list_display = (
        'img_preview',
        'post',
    )
    search_fields = ('post__slug', 'post__title',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'img_preview',
        'username',
        'first_name',
        'last_name',
        'email',
    )
    search_fields = ('username', 'first_name', 'last_name', 'email')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('img_preview', 'id', 'author', 'title', 'published_at', 'category', 'active')
    list_filter = ('category', 'published_at', 'author')
    search_fields = ('author', 'title', 'content')
    actions = ['activate', 'deactivate']

    inlines = [
        ImageFileInLine,
        CommentInLine,
    ]

    @admin.action
    def activate(self, request, queryset):
        queryset.update(active=True)

    @admin.action
    def deactivate(self, request, queryset):
        queryset.update(active=False)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'text', 'pub_date', 'active')
    list_filter = ('active', 'pub_date')
    search_fields = ('author', 'name', 'body')
    actions = ['approve_comments', 'reject_comments']

    @admin.action
    def approve_comments(self, request, queryset):
        queryset.update(active=True)

    @admin.action
    def reject_comments(self, request, queryset):
        queryset.update(active=False)
