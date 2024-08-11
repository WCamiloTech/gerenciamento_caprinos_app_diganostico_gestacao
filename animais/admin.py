# Register your models here.
from django.contrib import admin

from .models import DiagnosticoGestacao


@admin.register(DiagnosticoGestacao)
class DiagnosticoGestacaoAdmin(admin.ModelAdmin):
    list_display = ('brinco', 'data_cobertura', 'data_diagnostico', 'reprodutor', 'ultimo_parto', 'dias_gestacao', 'resultado')
    search_fields = ('brinco', 'reprodutor')
