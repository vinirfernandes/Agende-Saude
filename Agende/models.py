from django.db import models
from datetime import datetime
from django.contrib.auth.models import User 
from django.db import models 

class Profile(models.Model): 
        user = models.OneToOneField(User, on_delete=models.CASCADE) 
        telefone = models.CharField(max_length=15) 
        data_nascimento = models.DateField() 
        cpf = models.CharField(max_length=11, unique=True) 
        cep = models.CharField(max_length=10) 
        numero = models.CharField(max_length=10) 
        uf = models.CharField(max_length=2) 
        cidade = models.CharField(max_length=100) 
        complemento = models.CharField(max_length=255, blank=True, null=True) 



class Clinica(models.Model): 
        user = models.OneToOneField(User, on_delete=models.CASCADE) 
        telefone = models.CharField(max_length=15) 
        cnpj = models.CharField(max_length=14, unique=True) 
        cep = models.CharField(max_length=10) 
        numero = models.CharField(max_length=10) 
        uf = models.CharField(max_length=2) 
        cidade = models.CharField(max_length=100) 
        complemento = models.CharField(max_length=255, blank=True, null=True)
        latitude = models.FloatField()
        longitude = models.FloatField()