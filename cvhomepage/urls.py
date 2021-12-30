from django.urls import path
from .import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('blogs', views.blogPage, name='blog'),
    path('blog', views.singleBlogPage, name='single_blog'),
]
