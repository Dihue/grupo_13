from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from .models import User

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        field = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email',
            'birthdate'
        ]

class EditUserForm(UserChangeForm):
    model = User
    field = [
        'image',
        'password1',
        'password2',
        'first_name',
        'last_name',
        'email',
        'birthdate'
    ]