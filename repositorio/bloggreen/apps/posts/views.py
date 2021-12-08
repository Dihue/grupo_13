from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from .models  import Post, Comment


def like_view(request, pk):
    post = get_object_or_404(Post, id= request.POST.get('post_id'))
    liked = False
class PostListView(ListView):
    model=Post

class PostDetailView(DetailView):
    model=Post

class PostCreateView(CreateView):
    model=Post

class PostUpdateView(UpdateView):
    model=Post

class PostDeleteView(DeleteView):
    model=Post