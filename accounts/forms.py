from django import forms
from django.contrib.auth.models import User

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        verbose_name = 'Formulário De UserProfile'
        exclude = ['user']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        verbose_name = 'Formulário De User'
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class PasswordChangeForm(forms.ModelForm):
    class Meta:
        model = User
        verbose_name= 'Formulário alteração de senha de usuário'
        fields = ['username', 'password']