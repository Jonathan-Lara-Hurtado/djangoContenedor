from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'Subida'

urlpatterns = [
    path('', views.index, name='index'),
    path('modelos/', views.VistaSubidaModelos.as_view(), name='modelos')
]