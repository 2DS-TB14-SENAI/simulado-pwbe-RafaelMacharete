from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioAbs(AbstractUser):
    telefone = models.CharField(max_length=15)