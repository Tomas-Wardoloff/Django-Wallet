from django.db import models

from accounts.models import Account
from authentication.models import CustomUser
from categories.models import IncomeCategory, ExpenseCategory


class Income(models.Model):
    """
    Model for income transactions
    Atributes:
        amount: (DecimalField): The amount of money received.
        date: (DateField): The date when the income was received.
        user: (ForeignKey to CustomUser): Refrence to the CustomUser who received the income.
        user_account: (ForeignKey to Account): Refrence to the Account where the income was received.
        category: (ForeignKey to IncomeCategory): The category of the income, linked to IncomeCategory.
        description: (CharField): Optional description of the income.
        
    Meta:
        db_table: Specifies the name of the database table ('incomes').

    Methods:
        __str__: Returns a string representation of the income.
    """
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta():
        db_table = 'incomes'

    def __str__(self):
        return f'Income(ID: {self.id}, Amount: ${self.amount}, User: {self.user}, Date: {self.date})'


class Expense(models.Model):
    """
    Model for expense transactions
    Attributes:
        amount: (DecimalField): The amount of money spent.
        date: (DateField): The date when the expense was made.
        user: (ForeignKey to CustomUser): Reference to the CustomUser who made the expense.
        user_account: (ForeignKey to Account): Reference to the Account where the expense was made.
        category: (ForeignKey to ExpenseCategory): The category of the expense, linked to ExpenseCategory.
        description: (CharField): Optional description of the expense.
        
    Meta:
        db_table: Specifies the name of the database table ('expenses').

    Methods:
        __str__: Returns a string representation of the expense.
    """
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta():
        db_table = 'expenses'

    def __str__(self):
        return f'Expense(ID: {self.id}, Amount: ${self.amount}, User: {self.user}, Date: {self.date})'


class Transfer(models.Model):
    """
    Model for transfer transactions
    Attributes:
        amount: (DecimalField): The amount of money transferred.
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
    amount = models.DecimalField(max_digits=10, decimal_places=2)
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
