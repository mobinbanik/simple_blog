from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post/create/', create_post, name='post-create'),
    path('post/edit/<int:_id>/', edit_post, name='post-edit'),
    path('post/delete/<int:_id>/', delete_post, name='post-delete'),
    path('post/<str:slug>/', show_post, name='post'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('search/', search, name='search'),
    path('<str:category_name>/', category, name='category'), #TODO create dynamic

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
