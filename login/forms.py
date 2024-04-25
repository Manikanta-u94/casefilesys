from django import forms
from django.contrib.auth.forms import AuthenticationForm

class SignInForm(AuthenticationForm):
    username = forms.CharField(label = 'Username ', max_length = 25,
                            widget=forms.TextInput(attrs={
                                "class": "form-control","placeholder": "Enter your password"}))
    password = forms.CharField(
                            widget=forms.PasswordInput(attrs={
                                "class": "form-control","placeholder": "Enter your password"}))