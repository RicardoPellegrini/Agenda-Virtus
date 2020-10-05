from django.db import models


class Contato(models.Model):
  nome = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  telefone = models.CharField(max_length=15)
  criado = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.nome

class Endereco(models.Model):
  cep = models.CharField(max_length=9)
  logradouro = models.CharField(max_length=60)
  complemento = models.CharField(max_length=40)
  localidade = models.CharField(max_length=40)
  estado = models.CharField(max_length=2)
  contato = models.ForeignKey(Contato, on_delete=models.CASCADE, default=None)
  criado = models.DateField(auto_now_add=True)





