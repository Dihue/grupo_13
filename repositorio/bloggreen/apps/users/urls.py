from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('registro/', views.RegisterUser.as_view(), name='registro')
    
]