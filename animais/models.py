from django.db import models

# Create your models here.

class DiagnosticoGestacao(models.Model):
    brinco = models.CharField(max_length=20)
    data_cobertura = models.DateField()
    data_diagnostico = models.DateField()
    reprodutor = models.CharField(max_length=100)
    ultimo_parto = models.DateField()
    dias_gestacao = models.IntegerField()
    resultado = models.CharField(max_length=20)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.brinco} - {self.resultado}'
