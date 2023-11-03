from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserCreationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = ["username", "address", "phone_number", "password1", "password2"]

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data["username"] = cleaned_data["username"].lower()
        return cleaned_data


class LoginForm(AuthenticationForm):
    def clean_username(self):
        # Ensure the username is treated as lowercase
        return self.cleaned_data["username"].lower()


class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = ["amount"]
