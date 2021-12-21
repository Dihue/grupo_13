from django.urls import path
from apps.posts.views import *

app_name = "posts"

urlpatterns = [
    path('post/crear', PostCreateView.as_view(), name='crearPost'),
    path('post/<int:pk>', PostShowView.as_view(), name='mostrarPost'),
    path('post/editar/<int:pk>', PostEditView.as_view(), name='editarPost'),
    path('post/eliminar/<str:pk>', PostDeleteView.as_view(), name='deletePost'),
    path('post/like/<str:pk>', like_view, name='likesPost'),
    path('post/dislike/<str:pk>', dislike_view, name='dislikesPost'),
    path('post/listar/fecha', PostListView.as_view(), name='listarPost'),
    path('post/<int:pk>/crear_comment/', PostComment.as_view(), name='nuevoComentario'),
    path('busqueda', postSearchView, name = 'buscarPost'),
    path('categoria', postCategoryView, name = 'categoriaPost'),
    path('post/listar/comentario', post_comentarios, name='listarPost2')
]