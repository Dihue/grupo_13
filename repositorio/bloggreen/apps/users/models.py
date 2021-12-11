from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

# Create your models here.

def validar_extension(valor):
    if not valor.name.endswith(settings.ALLOWED_IMG):
        raise ValidationError("Este formato de imagen no es valido")

class NewUser(AbstractUser):
    image = models.ImageField(upload_to = 'perfil',
     null=True, blank=True, default=None, validators=[validar_extension])
    is_superuser = models.BooleanField(default = False)
    is_writer = models.BooleanField(default = False)
    is_reader = models.BooleanField(default = True)
    birthday = models.DateField(null=True, default=None)
