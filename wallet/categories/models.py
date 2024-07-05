from django.db import models

from authentication.models import CustomUser


class IncomeCategory(models.Model):
    """
    Represents an income category.

    Attributes:
        name (str): The name of the income category.
        is_default (bool): Indicates whether the income category is a default category.
        user (CustomUser): The user associated with the income category.

    Meta:

        db_table (str): Specifies the name of the database table ('income_categories').

    Methods:
        __str__(): Returns a string representation of the income category.
    """

    name = models.CharField(max_length=50)
    is_default = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta():
        db_table = 'income_categories'

    def __str__(self) -> str:
        if self.is_default:
            return f"IncomeCategory(ID: {self.id}, Name: {self.name}, Default: {self.is_default})"
        return f"IncomeCategory(ID: {self.id}, Name: {self.name}, User: {self.user})"


class ExpenseCategory(models.Model):
    """
    Represents an expense category.

    Attributes:
        name (str): The name of the expense category.
        is_default (bool): Indicates whether the category is a default category.
        user (CustomUser): The user associated with the category.

    Meta:
        db_table (str): Specifies the name of the database table ('expense_categories').

    Methods:
        __str__(): Returns a string representation of the expense category.
    """

    name = models.CharField(max_length=50)
    is_default = models.BooleanField(default=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta():
        db_table = 'expense_categories'

    def __str__(self) -> str:
        if self.is_default:
            return f"ExpenseCategory(ID: {self.id}, Name: {self.name}, Default: {self.is_default})"
        return f"ExpenseCategory(ID: {self.id}, Name: {self.name}, User: {self.user})"
