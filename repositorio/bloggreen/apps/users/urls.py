from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('registro/', views.RegisterUser.as_view(success_url = reverse_lazy('usuarios:registrar_completo')), name='registro'),
    path('login/', LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    
]
