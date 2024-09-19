from django.urls import path

from . import views

urlpatterns = [
    path('', views.listar_diagnosticos, name='listar_diagnosticos'),
    path('adicionar/', views.adicionar_diagnostico, name='adicionar_diagnostico'),
    path('diagnostico/editar/<int:pk>/', views.editar_diagnostico, name='editar_diagnostico'),
]
