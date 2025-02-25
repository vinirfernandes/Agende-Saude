"""
URL configuration for AgendeSaude project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Agende.views import register_user, login_view, register_clinica, success, base, mapa_clinica



# COLOCAR AS PAGINAS DE LOGIN E CADASTRO
# LOGIN
# SIGNUP
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', register_user, name='register'),
    path('registerclinica/', register_clinica, name='register'),
    path('success/<str:nome>/', success, name='success'),
    path('base.html/', base, name='base.html'),
    path('mapa/', mapa_clinica, name='mapa_clinica'),
]


