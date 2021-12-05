from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from .models import User

class RegisterUserForm(UserCreationForm):
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