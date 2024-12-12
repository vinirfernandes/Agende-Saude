from django import forms
from django.contrib.auth.models import User

class RegisterProfileForm(forms.ModelForm):
    telefone = forms.CharField(max_length=15)
    data_nascimento = forms.DateField(input_formats=["%d/%m/%Y"])
    cpf = forms.CharField(max_length=11)
    cep = forms.CharField(max_length=10)
    numero = forms.CharField(max_length=10)
    uf = forms.CharField(max_length=2)
    cidade = forms.CharField(max_length=100)
    complemento = forms.CharField(max_length=255, required=False)
    senha = forms.CharField(widget=forms.PasswordInput)
  
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'senha']



class RegisterClinicaForm(forms.ModelForm):
    telefone = forms.CharField(max_length=15)
    cnpj = forms.CharField(max_length=11)
    cep = forms.CharField(max_length=10)
    numero = forms.CharField(max_length=10)
    uf = forms.CharField(max_length=2)
    cidade = forms.CharField(max_length=100)
    complemento = forms.CharField(max_length=255, required=False)
    senha = forms.CharField(widget=forms.PasswordInput)
  
    class Meta:
        model = User
        fields = ['email', 'first_name', 'senha']

