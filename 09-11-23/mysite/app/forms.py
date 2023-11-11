from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import App


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


class UserRegistionForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    password = forms.CharField(
        required=True, label="Password", widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        required=True, label="Password Confirmation", widget=forms.PasswordInput()
    )

    def clean_password2(self):
        pass1 = self.cleaned_data.get("password")
        pass2 = self.cleaned_data.get("password2")
        if pass1 != pass2:
            raise (forms.ValidationError("Comform password is not match"))
        else:
            return pass2
