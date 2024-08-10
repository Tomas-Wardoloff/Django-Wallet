from rest_framework import serializers

from .models import Expense, Transfer, Income
from accounts.serializers import AccountSerializer
from authentication.serializers import CustomUserSerializer
from categories.serializers import ExpenseCategorySerializer, IncomeCategorySerializer


class IncomeSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    user_account = AccountSerializer()
    category = IncomeCategorySerializer()

    class Meta:
        model = Income
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    user_account = AccountSerializer()
    category = ExpenseCategorySerializer()

    class Meta:
        model = Expense
        fields = '__all__'


class TransferSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()
    from_user_account = AccountSerializer()
    to_user_account = AccountSerializer()

    class Meta:
        model = Transfer
        fields = '__all__'
