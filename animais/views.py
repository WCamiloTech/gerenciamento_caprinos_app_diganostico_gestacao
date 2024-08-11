# Create your views here.
from django.shortcuts import redirect, render

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
