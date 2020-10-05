from django.urls import path
from .views import *

urlpatterns = [
  # Lista de todos os contatos
  path('lista/', lista_contatos, name="lista_contatos"),

  # CRUD dos contatos
  path('', formulario_contato, name="cria_contato"),
  path('<int:id>/', formulario_contato, name="atualiza_contato"),
  path('deletacontato/<int:id>/', deleta_contato, name="deleta_contato"),

  # CRUD dos endereços
  path('endereco/', formulario_endereco, name="cria_endereco"),
  path('endereco/<int:id>/', formulario_endereco, name="atualiza_endereco"),
  path('deletaendereco/<int:id>/', deleta_endereco, name="deleta_endereco"),
]