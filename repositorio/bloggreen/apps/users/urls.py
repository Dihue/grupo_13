from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.RegisterUser.as_view(), name='registro')
    
]
