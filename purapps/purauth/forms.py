"""Purauth forms module."""
from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class UserCreationForm(auth_forms.UserCreationForm):
    """User creation form class."""

    class Meta(auth_forms.UserCreationForm.Meta):
        """User creation form meta class."""

        model = get_user_model()


class InscriptForm(auth_forms.UserCreationForm):
    """Inscription form."""

    email = forms.CharField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control me-2",
                "input_type": "email",
                "placeholder": "Email",
            }
        ),
    )
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control me-2",
                "placeholder": "Pseudo",
            }
        ),
    )
    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control me-2",
                "placeholder": "***********",
                "input_type": "password",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control me-2",
                "placeholder": "***********",
                "input_type": "password",
            }
        ),
    )

    class Meta:
        """InscriptForm meta class."""

        model = get_user_model()
        fields = ("username", "email", "password1", "password2")


class NewLoginForm(auth_forms.UserCreationForm):
    """Login form."""

    email = forms.EmailField(
        max_length=200,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control me-2",
                "placeholder": "Email",
            }
        ),
    )

    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control me-2",
                "placeholder": "Mot de passe",
            }
        ),
    )

    class Meta:
        """LoginForm meta class."""

        model = get_user_model()
        fields = ("email", "password")


class PremiumForm(forms.Form):
    """Premium form."""

    premium = forms.CharField(
        label="",
        max_length=1,
        widget=forms.HiddenInput(
            attrs={
                "class": "form-control me-2",
                "id": "confirm",
                "placeholder": "",
                "value": "1",
            }
        ),
    )

    def clean_premium(self):
        """Clean premium."""
        data = self.cleaned_data["premium"]

        if data != "1":
            raise ValidationError(
                "You must not modify the default content of the value: 1"
            )
        return data
