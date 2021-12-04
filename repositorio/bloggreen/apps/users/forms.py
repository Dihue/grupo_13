from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from .models import User

from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birthdate = forms.DateField()

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
        ]

class EditUserForm(UserChangeForm):
    model = User
    fields = [
        'image',
        'password1',
        'password2',
        'first_name',
        'last_name',
        'email',
        'birthdate'
    ]