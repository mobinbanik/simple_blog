from django.urls import path
from .views import *

urlpatterns = [
    path('', say_hello, name='say_hello')
]
