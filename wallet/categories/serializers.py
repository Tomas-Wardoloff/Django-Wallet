from rest_framework import serializers

from authentication.serializers import CustomUserSerializer
from .models import IncomeCategory, ExpenseCategory


class IncomeCategorySerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = IncomeCategory
        fields = '__all__'


class ExpenseCategorySerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = ExpenseCategory
        fields = '__all__'
