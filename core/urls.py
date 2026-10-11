
from django.urls import path
from . import views



urlpatterns = [
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('cadastrar/', views.cadastrar_projeto, name='cadastrar_projeto'),
    path('editar/<int:pk>/', views.editar_projeto, name='editar_projeto'),
    path('excluir/<int:pk>/', views.excluir_projeto, name='excluir_projeto'),
]
