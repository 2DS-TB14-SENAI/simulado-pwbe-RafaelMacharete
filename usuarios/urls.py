from django.urls import path
from . import views

urlpatterns = [
    path('auth/registro/', views.criar_usuario, name='logar'),
    path('auth/login/', views.logar, name='logar'),
]
