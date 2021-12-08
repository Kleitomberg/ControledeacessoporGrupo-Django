from django.urls import path

from .views import CreateCampo, CreateAtividade, UpdateAtividade, UpdateCampo, DeleteAtividade, DeleteCampo
from .views import ListAtividade, ListCampo

urlpatterns = [

    path('cadastrar/campo/',CreateCampo.as_view(), name='cadastrar-Campo'),
    path('cadastrar/atividade/', CreateAtividade.as_view(), name='cadastrar-Atividade'), 
    path('editar/campo/<int:pk>/', UpdateCampo.as_view(), name='editar-Campo'),
    path('editar/atividade/<int:pk>/', UpdateAtividade.as_view(), name='editar-Atividade'),
    path('deletar/atividade/<int:pk>/', DeleteAtividade.as_view(), name='deletar-Atividade'),
    path('deletar/campo/<int:pk>/', DeleteCampo.as_view(), name='deletar-campo'),

    path('listar/campos', ListCampo.as_view(), name='listar-campos'),
    path('listar/atividades', ListAtividade.as_view(), name='listar-Atividades')

]