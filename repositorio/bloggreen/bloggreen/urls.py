from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',views.Inicio, name='inicio'),
    path('',include('apps.users.urls')),
    path('',include('apps.posts.urls')),
    path('perfil/',views.Perfil, name='perfil'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
