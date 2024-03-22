from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, TitleViewSet

router_post = DefaultRouter()
router_post_title = DefaultRouter()
router_post.register(r'blogposts', BlogPostViewSet)
router_post_title.register(r'blogposts', TitleViewSet)

urlpatterns = [
    path('', include(router_post.urls)),
    path('title/', include(router_post_title.urls)),
]
