from django.db import models
from django.core.exceptions import ValidationError

from djmoney.models.fields import MoneyField

from accounts.models import Account
from authentication.models import CustomUser
from categories.models import Category


class Transaction(models.Model):
    """
    Model for income or expense transactions
    Atributes:
        amount: (MoneyField): The amount of money received.
        date: (DateField): The date when the income was received.
        user: (ForeignKey to CustomUser): Refrence to the CustomUser who received the income.
        user_account: (ForeignKey to Account): Refrence to the Account where the income was received.
        category: (ForeignKey to Category): The category of the transaction, linked to Category.
        description: (CharField): Optional description of the income.

    Meta:
        db_table: Specifies the name of the database table ('incomes').

    Methods:
        __str__: Returns a string representation of the income.
    """
    amount = MoneyField(max_digits=10, decimal_places=2,
                        default_currency='USD')
    date = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta():
        db_table = 'transactions'

    def __str__(self):
        if self.category.type == 'Income':
            return f'Income(ID: {self.id}, Amount: {self.amount}, User: {self.user}, Date: {self.date})'
        return f'Expense(ID: {self.id}, Amount: {self.amount}, User: {self.user}, Date: {self.date})'

    def clean(self):
        super().clean()
        if self.user != self.user_account.user:
            raise ValidationError(
                {'user_account': 'The account does not belong to the user'})
        if self.category.user and self.user != self.category.user:
            raise ValidationError(
                {'category': 'The category is not a default category or does not belong to the user'})

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Transfer(models.Model):
    """
    Model for transfer transactions
    Attributes:
        amount: (MoneyField): The amount of money transferred.
        date: (DateField): The date when the transfer was made.
        user: (ForeignKey to CustomUser): Reference to the CustomUser who initiated the transfer.
        from_user_account: (ForeignKey to Account): Reference to the Account where the money was transferred from.
        to_user_account: (ForeignKey to Account): Reference to the Account where the money was transferred to.
        description: (CharField): Optional description of the transfer.

    Meta:
        db_table: Specifies the name of the database table ('transfers').

    Methods:
        __str__: Returns a string representation of the transfer.
    """
    amount = MoneyField(max_digits=10, decimal_places=2,
                        default_currency='USD')
    date = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    from_user_account = models.ForeignKey(
        Account, related_name='transfers_out', on_delete=models.CASCADE)
    to_user_account = models.ForeignKey(
        Account, related_name='transfers_in', on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta():
        db_table = 'transfers'

    def __str__(self):
        return f'Transfer(ID: {self.id}, Amount: ${self.amount}, User: {self.user}, Date: {self.date}, From: {self.from_user_account}, To: {self.to_user_account})'

    def clean(self):
        super().clean()
        if self.user != self.from_user_account.user or self.user != self.to_user_account.user:
            raise ValidationError(
                'The accounts involved do not belong to the user')
        if self.from_user_account == self.to_user_account:
            raise ValidationError(
                'The accounts involved are the same')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
