from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

app_name = "users"

urlpatterns = [
    path('registro/', views.RegisterUser.as_view(success_url = reverse_lazy('users:registro_completo')), name='registro'),
    path('registro/finalizado', views.RegisterUser.as_view(template_name = "usuario/registroCompleto.html"), name = 'registro_completo'),
    path('login/', LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    path('EditarUsuario/', views.EditUser.as_view(), name = "editar"),
]
