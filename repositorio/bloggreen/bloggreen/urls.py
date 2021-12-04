from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from . import views

from apps.posts.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
        
    path('',views.Inicio, name='inicio'),
    path('',include('apps.users.urls'))
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


'''
    path('lista/', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<slug>/', PostDetailView.as_view(), name='detail'),
    path('<slug>/update/', PostUpdateView.as_view(), name='update'),
    path('<slug>/delete/', PostDeleteView.as_view(), name='delete'),
'''