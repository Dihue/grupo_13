from django.shortcuts import render
from apps.posts.models import Post

def Inicio(request):
    post = Post.objects.filter().last()
    context = {'post':post}
    return render(request, 'index.html', context)

def Login(request):
    return render(request,'usuarios/login.html')

def Perfil(request):
    args = {'user': request.user}
    print(args)
    return render(request, 'usuario/perfil.html', args)
