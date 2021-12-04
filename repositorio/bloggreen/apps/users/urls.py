from django.urls import path
from . import views
from django.urls import reverse_lazy

urlpatterns = [
    path('registro/', views.RegisterUser.as_view(success_url = reverse_lazy('inicio')), name='registro')

]