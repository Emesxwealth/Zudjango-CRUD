from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import PostListView
from .models import BlogApp, Post


class BlogAppPostListView(PostListView):
    model = Post
    fields = ["__all__"]
    success_url  = reverse_lazy("blog:all")

class BlogAppPostDetailView(PostDetailView):
    model = Post

class BlogAppPostUpdateView(PostUpdateView): 
    model = Post
    fields = ["__all__"]
    success_url  = reverse_lazy("blog:all")   

class BlogAppPostDeleteView(PostDeleteView):
    model = Post
    fields = ["__all__"]
    success_url  = reverse_lazy("blog:all")  


