from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserLoginForm(forms.Form):
    """
    A form for user login.

    This form is used to authenticate users by requesting their email and password.

    Attributes:
        email (EmailField): The field for entering the user's email.
        password (CharField): The field for entering the user's password.
    """
    email = forms.EmailField(help_text='Enter your email', required=True)
    password = forms.CharField(
        widget=forms.PasswordInput(),
        help_text='Enter your password',
        required=True)


class CustomUserCreationForm(UserCreationForm):
    """
    A form for creating a new user.

    This form extends the built-in UserCreationForm provided by Django
    and adds additional fields for first name, last name, and email.

    Attributes:
        model (CustomUser): The model class representing the user.
        fields (list): The list of fields to include in the form.
    """
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
