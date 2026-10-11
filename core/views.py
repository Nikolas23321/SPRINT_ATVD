

from django.shortcuts import render, redirect
from .models import Projeto
from .forms import ProjetoForm
from django.contrib import messages



def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'lista_projetos.html', {'projetos': projetos})


def cadastrar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto cadastrado com sucesso!')
            return redirect('/projetos/')
    else:
        form = ProjetoForm()

    return render(request, 'cadastrar_projeto.html', {'form': form})



def editar_projeto(request, pk):
    projeto = Projeto.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('/projetos/')

    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'editar_projeto.html', {'form': form})



def excluir_projeto(request, pk):
    projeto = Projeto.objects.get(pk=pk)
    projeto.delete()
    messages.success(request, 'Projeto excluído com sucesso!')
    return redirect('/projetos/')

