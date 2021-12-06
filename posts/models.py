#posts models

from django.db import models

# Create your models here.

class User(models.Model):
    #User model
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True,null=True) #No trae la hora

    created = models.DateTimeField(auto_now_add=True) #Viene con hora tambien
    modified = models.DateTimeField(auto_now=True)