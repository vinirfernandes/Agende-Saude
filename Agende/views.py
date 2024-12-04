from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# TODO RENDERIZAR AS PÁGINAS DE LOGIN OU CADASTRO

def register_user(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)        
            if form.is_valid():
                form.save()
                return redirect('Login')
            else:
                form = UserCreationForm()
                

    else:   
        form = UserCreationForm()
        return render(request, 'register/register_user.html', {'form': form})

def login_view(resquest):
    return render(resquest, 'login.html')
    

    