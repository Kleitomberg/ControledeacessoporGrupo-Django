from django.urls import path

from django.contrib.auth import views as auth_views 
from .views import CreateUsuario, PerfilUpdate

urlpatterns = [

path('login/',auth_views.LoginView.as_view(
    template_name='usuarios/login.html'
), name='login'),
path('logout/',auth_views.LogoutView .as_view(), name='logout'),
path('cadastro/',CreateUsuario.as_view(), name='cadastro'),
path('atualizar-dados/',PerfilUpdate.as_view(), name='atualizar-dados'),
    
]