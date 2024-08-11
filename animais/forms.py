from django import forms

from .models import DiagnosticoGestacao


class DiagnosticoGestacaoForm(forms.ModelForm):
    class Meta:
        model = DiagnosticoGestacao
        fields = '__all__'
