from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='posts'),
    path('post/create', create_post, name='post-create'),
    path('post/edit/<int:_id>/', edit_post, name='post-edit'),
    path('post/delete/<int:_id>/', delete_post, name='post-delete'),
    path('post/<int:_id>/', show_post, name='post'),
]
