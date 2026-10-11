from django.shortcuts import render
from .models import Projeto


def lista_projetos(request):
    return render(request, 'lista_projetos.html')


def cadastrar_projeto(request):
    return render(request, 'cadastrar_projeto.html')



def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'lista_projetos.html', {'projetos': projetos})


def cadastrar_projeto(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        data_inicio = request.POST['data_inicio']

        Projeto.objects.create(
            nome=nome,
            descricao=descricao,
            data_inicio=data_inicio
        )

    return render(request, 'cadastrar_projeto.html')
