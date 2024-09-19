from django.urls import path

from . import views
from .views import (adicionar_diagnostico, editar_diagnostico,
                    excluir_diagnostico, listar_diagnosticos)

urlpatterns = [
    path('', views.listar_diagnosticos, name='listar_diagnosticos'),
    path('adicionar/', views.adicionar_diagnostico, name='adicionar_diagnostico'),
    path('diagnostico/editar/<int:pk>/', views.editar_diagnostico, name='editar_diagnostico'),
    path('excluir/<int:pk>/', excluir_diagnostico, name='excluir_diagnostico'),
]
