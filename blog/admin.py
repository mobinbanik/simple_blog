from django.contrib import admin
from .models import Post, Category, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'published_at', 'category', 'active')
    list_filter = ('category', 'published_at', 'author')
    search_fields = ('author', 'title', 'content')
    actions = ['activate', 'deactivate']

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
