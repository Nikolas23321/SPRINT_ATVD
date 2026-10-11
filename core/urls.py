from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('cadastrar/', views.cadastrar_projeto, name='cadastrar_projeto'),
    path('editar/<int:pk>/', views.editar_projeto, name='editar_projeto'),
    path('excluir/<int:pk>/', views.excluir_projeto, name='excluir_projeto'),

    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
    path('tarefas/nova/', views.criar_tarefa, name='criar_tarefa'),
    path('tarefas/<int:pk>/editar/', views.editar_tarefa, name='editar_tarefa'),
    path('tarefas/<int:pk>/excluir/', views.excluir_tarefa, name='excluir_tarefa'),
]
