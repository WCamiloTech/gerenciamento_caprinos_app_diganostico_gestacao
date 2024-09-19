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
