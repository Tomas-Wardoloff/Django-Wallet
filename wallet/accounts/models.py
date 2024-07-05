from django.db import models

from authentication.models import CustomUser


class Account(models.Model):
    """
    Represents a user's account.

    Attributes:
        balance (DecimalField): The current balance of the account.
        name (CharField): The name of the account.
        user (ForeignKey): Reference to the CustomUser who owns the account.

    Meta:
        db_table: Specifies the name of the database table ('accounts').

    Methods:
        __str__: Returns a string representation of the account.
    """    
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=50)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta():
        db_table = 'accounts'

    def __str__(self):
        return f'Account(ID: {self.id}, Name: {self.name}, User: {self.user})'
