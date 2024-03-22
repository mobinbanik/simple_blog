from django.contrib import admin
from .models import Post, Category, Comment


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'body', 'post', 'created_on', 'active')
    # list_filter = ('active', 'created_on')
    # search_fields = ('name', 'email', 'body')
    # actions = ['approve_comments']
    #
    # def approve_comments(self, request, queryset):
    #     queryset.update(active=True)
