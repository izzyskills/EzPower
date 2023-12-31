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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input"


class LoginForm(AuthenticationForm):
    def clean_username(self):
        # Ensure the username is treated as lowercase
        return self.cleaned_data["username"].lower()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "input"


class TransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        fields = ["amount"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["amount"].widget.attrs["id"] = "amount"
        self.fields["amount"].widget.attrs["class"] = "input"


class AccountRechargeForm(forms.Form):
    payment_choices = [(1, "Credit Card"), (2, "Remita"), (3, "Bank Transfer")]
    payment_method = forms.ChoiceField(
        widget=forms.RadioSelect, required=True, choices=payment_choices
    )
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={"class": "input"}))
