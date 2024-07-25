from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Defines how the CustomUser model will create users and superusers.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Creates a new user with the given email, password, and additional fields.

        Parameters:
            email (str): The email address of the user.
            password (str): The password for the user account.
            **extra_fields: Additional fields to be saved for the user.

        Raises:
            ValueError: If the email is not provided.

        Returns:
            User: The newly created user object.
        """
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates a new superuser with the given email, password and additional fields.

        Parameters:
            email (str): The email address of the user.
            password (str): The password for the user account.
            **extra_fields: Additional fields to be saved for the user.

        Raises:
            ValueError: If the email is not provided.
            ValueError: If is_staff is not set to True for the superuser.
            ValueError: If is_superuser is not set to True for the superuser.

        Returns:
            User: The newly created user object.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)
