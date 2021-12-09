from django.db import models
from django.db.models import fields
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.conf import settings
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from apps.posts.forms import PostForm
from .models  import Post, Comment

def likeView(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    print(post)

    if post.like.filter(id = request.user.id).exists():
        print("hola2")
        post.like.remove(request.user)
        post.dislike.remove(request.user)
        liked = False
    else:
        print("hola3")
        post.like.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('posts:mostrarPost', args = [str(pk)]))

def dislikeView(request, pk):
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

    def formValid(self, form):
        form.instance.user = self.request.user

        if form.instance.thumbnail.name:
            ext = form.instance.portada.name.split(".")[-1]
            form.instance.thumbnail.name = form.instance.title + '.' + ext

        return super().formValid(form)

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

    def formValid(self, form):
        form.instance.usuario = self.request.user

        if form.instance.thumbnail.name:
            ext = form.instance.portada.name.split(".")[-1]
            form.instance.thumbnail.name = form.instance.title + '.' + ext

        return super().formValid(form)

class PostListView(ListView):
    model = Post
    paginate_by = 5
    ordering = ['-publish_date']
    #template_name = 'post/postList.html'
    template_name = 'index.html'
    context_object_name = 'posts'

    def latestPost(request):
        latest = Post.objects.filter(publish_date = timezone.now()).reverse()[:1]
        return render(request, 'index.html', {'latest' : latest})

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

'''
def like_view(request, pk):
    post = get_object_or_404(Post, id= request.POST.get('post_id'))
    liked = False
class PostListView(ListView):
    model=Post

def postListIndex(request):
    posts = Post.objects.order_by('-publish_date')
    return render(request, 'index.html', {'post':posts})

class PostDetailView(DetailView):
    model=Post

class PostCreateView(CreateView):
    model=Post

class PostUpdateView(UpdateView):
    model=Post

class PostDeleteView(DeleteView):
    model=Post
'''


