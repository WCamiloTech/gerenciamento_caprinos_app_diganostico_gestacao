from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import DiagnosticoGestacaoForm
from .models import DiagnosticoGestacao


def listar_diagnosticos(request):
    diagnosticos = DiagnosticoGestacao.objects.all()
    return render(request, 'animais/listar_diagnosticos.html', {'diagnosticos': diagnosticos})

def adicionar_diagnostico(request):
    if request.method == 'POST':
        form = DiagnosticoGestacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_diagnosticos')
    else:
        form = DiagnosticoGestacaoForm()
    return render(request, 'animais/adicionar_diagnostico.html', {'form': form})

def editar_diagnostico(request, pk):
    diagnostico = get_object_or_404(DiagnosticoGestacao, pk=pk)
    
    if request.method == 'POST':
        form = DiagnosticoGestacaoForm(request.POST, instance=diagnostico)
        if form.is_valid():
            form.save()
            return redirect('listar_diagnosticos')
    else:
        form = DiagnosticoGestacaoForm(instance=diagnostico)
    
    # Certifique-se de que o template está na pasta correta
    return render(request, 'animais/editar_diagnostico.html', {'form': form})

#Busca
def listar_diagnosticos(request):
    query = request.GET.get('q')
    if query:
        # Filtra os diagnósticos de acordo com o campo de pesquisa
        diagnosticos = DiagnosticoGestacao.objects.filter(
            Q(brinco__icontains=query) |
            Q(reprodutor__icontains=query) |
            Q(resultado__icontains=query)
        )
    else:
        # Caso não haja pesquisa, mostra todos os diagnósticos
        diagnosticos = DiagnosticoGestacao.objects.all()
    
    return render(request, 'animais/listar_diagnosticos.html', {'diagnosticos': diagnosticos})



def excluir_diagnostico(request, pk):
    diagnostico = get_object_or_404(DiagnosticoGestacao, pk=pk)
    if request.method == 'POST':
        diagnostico.delete()
        return redirect('listar_diagnosticos')
    else:
        # Normalmente não chegaria aqui, pois é uma exclusão via POST, mas podemos redirecionar para a lista de diagnósticos em caso de acesso indevido.
        return redirect('listar_diagnosticos')
