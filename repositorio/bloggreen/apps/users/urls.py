from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('registro/', views.RegisterUser.as_view(), name='registro'),

]
