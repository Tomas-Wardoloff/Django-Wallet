# Generated by Django 5.0.6 on 2024-08-11 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_remove_expensecategory_user_and_more'),
        ('transactions', '0002_remove_income_category_remove_income_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExpenseCategory',
        ),
        migrations.DeleteModel(
            name='IncomeCategory',
        ),
    ]