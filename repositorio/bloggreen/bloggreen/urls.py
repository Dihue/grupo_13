from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from apps.users import views as viewsUser
from django.urls import reverse_lazy


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('lista/', PostListView.as_view(), name='list'),
    #path('create/', PostCreateView.as_view(), name='create'),
    #path('<slug>/', PostDetailView.as_view(), name='detail'),
    #path('<slug>/update/', PostUpdateView.as_view(), name='update'),
    #path('<slug>/delete/', PostDeleteView.as_view(), name='delete'),
    path('registro/', viewsUser.RegisterUser.as_view(success_url = reverse_lazy('usuarios:registrar_completo')), name='registro'),
    path('',views.Inicio, name='inicio'),
    path('usuarios',include('apps.users.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)