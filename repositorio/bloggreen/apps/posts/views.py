from django.db.models.expressions import OrderBy
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls.base import reverse_lazy
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.db.models import Q
from apps.posts.forms import PostForm, EditPostForm, CommentForm
from .models  import Categoria, Post, Comment
from apps.users.models import NewUser
from django.db.models import Count
from django.db.models import F

def like_view(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    liked = False
    print(post.like.filter(id = request.user.id).exists())

    if post.like.filter(id = request.user.id).exists():
        post.like.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        post.dislike.remove(request.user)
        liked = True

    return HttpResponseRedirect(reverse('posts:mostrarPost', args = [str(pk)]))

def dislike_view(request, pk):
    post = get_object_or_404(Post, id = request.POST.get('post_id'))
    disliked = False

    if post.dislike.filter(id = request.user.id).exists():
        post.dislike.remove(request.user)
        disliked = False
    else:
        post.dislike.add(request.user)
        post.like.remove(request.user)
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

class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'post/postEdit.html'
    success_url = reverse_lazy('inicio')
    login_url = settings.LOGIN_URL

    def form_valid(self, form):
        form.instance.user = self.request.user

        if form.instance.thumbnail.name:
            ext = form.instance.thumbnail.name.split(".")[-1]
            form.instance.thumbnail.name = form.instance.title + '.' + ext

        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.user
            

class MsjException(Exception):
    pass


def like_view(request, pk):
    post = get_object_or_404(Post, id= request.POST.get('post_id'))
    liked = False
class PostListView(ListView):
    model = Post
    ordering = ['-publish_date']
    template_name = 'post/postList.html'
    context_object_name = 'posts'
    
def post_comentarios(request):
    opcion = request.GET.get('select')
    posts = Post.objects.annotate(num_comments=Count('commentsPost')).order_by('-num_comments')

    return render(request,'post/postList.html', {'posts':posts})

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

class PostComment(LoginRequiredMixin, CreateView):
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

        return HttpResponseRedirect(reverse('posts:mostrarPost', args = [str(new.post_id)]))

#-------------------------------BUSCADOR----------------------------------------------------------

def search(request):
    return render(request, 'buscador.html')

def postSearchView(request):
    queryset = request.GET.get("buscar")

    resultados = {}
    categorias = Categoria.objects.all()
    resultados['categorias'] = categorias

    if queryset:
        user = NewUser.objects.filter(username = queryset)
        resultados['posts'] = Post.objects.filter(
            Q(title__icontains = queryset) |
            Q(user__in = user)
        ).distinct()

    return render(request,'buscador.html', resultados)

def postCategoryView(request):

    categoria_id = request.GET.get('filtro', None)

    resultados = {}
    categorias = Categoria.objects.all()
    resultados['categorias'] = categorias

    if categoria_id:
        posteos = Post.objects.filter(categoria_id = categoria_id)
        resultados['posts'] = posteos 

    return render(request,'post/postCategory.html', resultados)

