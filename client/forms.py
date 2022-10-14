from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput, label=('Parol takroran'))

    def clean_confirm(self):
        if self.cleaned_data["confirm"] != self.cleaned_data["password"]:
            raise ValidationError("Parollar bir xil emas!")

        return self.cleaned_data['confirm']

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            "username": ('Login '),
            "password": ('Parol')

        }

        help_texts = {
            "username": ("Lotin harflari, sonlar va @/#/$/%/^/&/_ belgilar iborat bo'lish lozim")
        }

        widgets = {
            'password': forms.PasswordInput
        }



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label=('<b>Login</b>'), required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput, label=('<b>Parol</b>'),  required=True)