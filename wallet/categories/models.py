from django.db import models

from authentication.models import CustomUser


class Category(models.Model):
    """
    Represents an income or expense category.

    Attributes:
        name (str): The name of the income category.
        is_default (bool): Indicates whether the income category is a default category.
        user (CustomUser): The user associated with the income category.
        type (str): The type of the income category.

    Meta:

        db_table (str): Specifies the name of the database table ('categories').

    Methods:
        __str__(): Returns a string representation of the income category.
    """
    CATEGORY_TYPE = [
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    ]
    
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    type = models.CharField(max_length=7, choices=CATEGORY_TYPE)
    
    class Meta():
        db_table = 'categories'

    def __str__(self) -> str:
        return self.name
