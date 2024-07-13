from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from .managers import CustomUserManager


class CustomUser(AbstractUser, PermissionsMixin):
    """
    CustomUser class representing a custom user model in Django.

    Inherits from:
        - AbstractUser: Django's built-in abstract user model.
        - PermissionsMixin: Django's built-in model for adding permission-related functionality.

    Attributes:
        - email (EmailField): The email address of the user.

    Attributes inherited from AbstractUser:
        - username (CharField): The username of the user.
        - first_name (CharField): The first name of the user.
        - last_name (CharField): The last name of the user.
        - is_staff (BooleanField): Designates whether the user can access the admin site.
        - is_active (BooleanField): Designates whether the user account is active.
        - date_joined (DateTimeField): The date and time when the user account was created.

    Attributes inherited from PermissionsMixin:
        - groups (ManyToManyField): The groups the user belongs to.
        - user_permissions (ManyToManyField): The permissions directly assigned to the user.

    Custom Manager:
        - objects (CustomUserManager): Custom manager for the CustomUser model.

    Custom Fields:
        - USERNAME_FIELD (str): The field used as the unique identifier for authentication (email in this case).
        - REQUIRED_FIELDS (list): List of fields required when creating a user (first_name, last_name).

    Methods:
        - __str__: Returns a string representation of the user.
        - save: Overrides the save method to set the username as 'user_<email>' when saving the user.
    """
    email = models.EmailField(help_text='User email address',
                              verbose_name='Email', unique=True, blank=False, null=False)
    username = models.CharField(max_length=150, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return f'User(ID: {self.id}, Email: {self.email})'

    def save(self, *args, **kwargs):
        self.username = f"user_{self.email}"
        super().save(*args, **kwargs)
