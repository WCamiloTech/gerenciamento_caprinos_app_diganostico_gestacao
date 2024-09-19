from django import forms

from .models import DiagnosticoGestacao


class DiagnosticoGestacaoForm(forms.ModelForm):
    class Meta:
        model = DiagnosticoGestacao
        fields = ['brinco', 'data_cobertura', 'data_diagnostico', 'reprodutor', 'ultimo_parto', 'dias_gestacao', 'resultado', 'observacao']
        
        widgets = {
            'data_cobertura': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'data_diagnostico': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'ultimo_parto': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(DiagnosticoGestacaoForm, self).__init__(*args, **kwargs)
        # Garantindo que os valores existentes sejam exibidos nos campos de data
        self.fields['data_cobertura'].input_formats = ['%Y-%m-%d']
        self.fields['data_diagnostico'].input_formats = ['%Y-%m-%d']
        self.fields['ultimo_parto'].input_formats = ['%Y-%m-%d']
