from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.

def validar_extension(valor):
    if not valor.name.endswith(settings.ALLOWED_IMG):
        raise ValidationError("Este formato de imagen no es valido")

class User(AbstractUser):
    image = models.ImageField(upload_to = 'perfil',
     null=True, blank=True, default=None, validators=[validar_extension])
