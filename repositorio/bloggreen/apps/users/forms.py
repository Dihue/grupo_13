from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django.forms import fields
from .models import NewUser
from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
        ]

class EditUserForm(UserChangeForm):
    class Meta:
        model = NewUser
        fields = [
            'image',
            'first_name',
            'last_name',
            'email',
        ]
