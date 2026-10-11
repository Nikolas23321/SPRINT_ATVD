from django.shortcuts import render, redirect
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm
from django.contrib import messages
from .models import Tarefa

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

def lista_tarefas(request):
    tarefas = Tarefa.objects.select_related('projeto').all()
    return render(request, 'core/lista_tarefas.html', {
        'tarefas': tarefas
    })

def criar_tarefa(request):
    form = TarefaForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tarefa cadastrada com sucesso!')
        return redirect('core:lista_tarefas')

    return render(request, 'core/form_tarefa.html', {'form': form})

def editar_tarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Tarefa atualizada com sucesso!')
        return redirect('core:lista_tarefas')

    return render(request, 'core/form_tarefa.html', {'form': form})

def excluir_tarefa(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)

    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('core:lista_tarefas')

    return render(request, 'core/confirmar_exclusao_tarefa.html', {
        'objeto': tarefa
    })