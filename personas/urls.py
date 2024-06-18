from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_persona, name='agregar'),
    path('descargar-csv/', views.descargar_csv, name='descargar_csv'),
]