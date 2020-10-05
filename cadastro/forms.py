from django import forms
from .models import Contato, Endereco

class ContatoForm(forms.ModelForm):
  class Meta:
    model = Contato
    fields = ('nome', 'email', 'telefone')
    widgets = {
      'nome': forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Digite o nome...'}),
      'email': forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Digite seu e-mail...'}),
      'telefone': forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Digite seu telefone...'})
    }


class EnderecoForm(forms.ModelForm):
  class Meta:
    model = Endereco
    fields = ('cep', 'logradouro', 'complemento', 'localidade', 'estado', 'contato')
    widgets = {
      'cep': forms.TextInput(attrs={'onblur': 'pesquisacep(this.value);', 'autocomplete': 'off', 'placeholder': 'Digite o CEP sem hífen...'}),
      'logradouro': forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Digite o CEP...'}),
      'complemento': forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Digite o complemento de seu endereço...'}),
      'localidade': forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Digite o CEP...'}),
      'estado': forms.TextInput(attrs={'autocomplete': 'off', 'placeholder': 'Digite o CEP...'}),
    }

  def __init__(self, *args, **kwargs):
    super(EnderecoForm, self).__init__(*args, **kwargs)
    self.fields['complemento'].required = False

