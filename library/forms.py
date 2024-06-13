from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'password1',
            'password2',
        )
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }