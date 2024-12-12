from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User 
from .forms import RegisterProfileForm, RegisterClinicaForm
from .models import Profile, Clinica


def register_user(request):
    if request.method == 'POST':
        form = RegisterProfileForm(request.POST)
        if form.is_valid():        
            user = User.objects.create(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=make_password(form.cleaned_data['senha']) 
            )

            Profile.objects.create(
                user=user,
                telefone=form.cleaned_data['telefone'],
                data_nascimento=form.cleaned_data['data_nascimento'],
                cpf=form.cleaned_data['cpf'],
                cep=form.cleaned_data['cep'],
                numero=form.cleaned_data['numero'],
                uf=form.cleaned_data['uf'],
                cidade=form.cleaned_data['cidade'],
                complemento=form.cleaned_data['complemento']
            )

            messages.success(request, "Cadastro realizado com sucesso!")
            return render(request, 'register/success.html')
        else:
            return render(request, 'register/register_user.html', {'form': form})
    else:
        form = RegisterProfileForm()
    return render(request, 'register/register_user.html', {'form': form}) 


def register_clinica(request):
    if request.method == 'POST':
        form = RegisterClinicaForm(request.POST)
        if form.is_valid():        
            user = User.objects.create(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                password=make_password(form.cleaned_data['senha']) 
            )

            Clinica.objects.create(
                user=user,
                telefone=form.cleaned_data['telefone'],
                cnpj=form.cleaned_data['cnpj'],
                cep=form.cleaned_data['cep'],
                numero=form.cleaned_data['numero'],
                uf=form.cleaned_data['uf'],
                cidade=form.cleaned_data['cidade'],
                complemento=form.cleaned_data['complemento']
            )

            messages.success(request, "Cadastro realizado com sucesso!")
            return render(request, 'register/success.html')
        else:
            return render(request, 'register/register_clinica.html', {'form': form})
    else:
        form = RegisterClinicaForm()
    return render(request, 'register/register_clinica.html', {'form': form}) 


def login_view(resquest):
    return render(resquest, 'login.html')

def success(request, nome=None):
    return render(request, 'success.html', {'nome': nome})

def base(resquest):
    return render(resquest, 'base.html')
    

    