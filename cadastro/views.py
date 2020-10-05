from django.shortcuts import render, redirect
from .forms import ContatoForm, EnderecoForm
from .models import Contato, Endereco

# GET de todos os contatos cadastrados
def lista_contatos(request):
  context = {
    'contatos': Contato.objects.all(),
    'enderecos': Endereco.objects.all()
  }
  return render(request, 'contatos_lista.html', context)

# GET de contato especifico ou POST de novo endereço
def formulario_endereco(request, id=0):
  if request.method == 'GET':
    if id==0:
      enderecoForm = EnderecoForm()
    else:
      endereco = Endereco.objects.get(pk=id)
      enderecoForm = EnderecoForm(instance=endereco)
    context = {
      'enderecoForm': enderecoForm,
    }
    return render(request, 'endereco_form.html', context)
  else:
    if id==0:
      enderecoForm = EnderecoForm(request.POST)
    else:
      endereco = Endereco.objects.get(pk=id)
      enderecoForm = EnderecoForm(request.POST, instance=endereco)

    if enderecoForm.is_valid():
      enderecoForm.save()
      return redirect(lista_contatos)

# GET de contato especifico ou POST de novo contato
def formulario_contato(request, id=0):
  if request.method == 'GET':
    if id==0:
      contatoForm = ContatoForm()
    else:
      contato = Contato.objects.get(pk=id)
      contatoForm = ContatoForm(instance=contato)
    context = {
      'contatoForm': contatoForm,
    }
    return render(request, 'contato_form.html', context)
  else:
    if id==0:
      contatoForm = ContatoForm(request.POST)
    else:
      contato = Contato.objects.get(pk=id)
      contatoForm = ContatoForm(request.POST, instance=contato)
      if contatoForm.is_valid():
        contatoForm.save()
        return redirect(lista_contatos)

    if contatoForm.is_valid():
      contatoForm.save()
      return redirect(formulario_endereco)


# DELETE de contato específico
def deleta_contato(request, id):
  contato = Contato.objects.get(pk=id)
  contato.delete()
  return redirect(lista_contatos)

# DELETE de endereço específico
def deleta_endereco(request, id):
  endereco = Endereco.objects.get(pk=id)
  endereco.delete()
  return redirect(lista_contatos)
