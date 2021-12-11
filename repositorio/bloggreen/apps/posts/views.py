from django import template
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.template import RequestContext
from apps.posts.forms import PostForm, CommentForm
from .models  import Post, Comment

def like_view(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False

    if post.like.filter(id = request.user.id).exists():
        post.like.remove(request.user)
        post.dislike.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('posts:mostrarPost', args = [str(pk)]))

def dislike_view(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    disliked = False

    if post.dislike.filter(id = request.user.id).exists():
        post.dislike.remove(request.user)
        post.like.remove(request.user)
        disliked = False
    else:
        post.dislike.add(request.user)
        disliked = True

    return HttpResponseRedirect(reverse('posts:mostrarPost', args = [str(pk)]))


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/postForm.html'
    success_url = reverse_lazy('inicio')
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        form.instance.user = self.request.user

        if form.instance.thumbnail.name:
            ext = form.instance.thumbnail.name.split(".")[-1]
            form.instance.thumbnail.name = form.instance.title + '.' + ext

        return super().form_valid(form)

class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = [
        'titulo',
        'contenido',
        'portada',
        'categoria'
    ]
    template_name = 'post/postEdit.html'
    success_url = reverse_lazy('mostrarPost')
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        if form.instance.portada.name:
            ext = form.instance.portada.name.split(".")[-1]
            form.instance.portada.name = form.instance.title + '.' + ext

        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    paginate_by = 5
    ordering = ['-publish_date']
    template_name = 'post/postList.html'
    #template_name = 'index.html'
    context_object_name = 'posts'
class PostShowView(DetailView):
    model = Post
    template_name = 'post/postShow.html'

    def getContextData(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        total_dislikes = stuff.total_dislikes()

        liked = False
        disliked = False
        if stuff.like.filter(id = self.request.user.id).exists():
            liked = True
        elif stuff.dislike.filter(id = self.request.user.id).exists():
            disliked = True

        context['total_likes'] = total_likes
        context['total_dislikes'] = total_dislikes
        context['liked'] = liked
        context['disliked'] = disliked

        return context  

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('inicio')

class PostCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/postCommentForm.html'
    success_url = reverse_lazy('inicio')
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        new = form.save(commit = False)
        new.post_id = self.kwargs['pk']
        new.user = self.request.user
        new.save()

        return HttpResponseRedirect(reverse('posts:mostrarPost', args = [str[new.post_id]]))


