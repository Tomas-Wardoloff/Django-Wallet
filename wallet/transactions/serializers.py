from django.core.exceptions import ValidationError

from rest_framework import serializers

from .models import Transaction, Transfer


class TransactionDetailSerializer(serializers.ModelSerializer):
    user = serializers.EmailField(source='user.email', read_only=True)
    user_account = serializers.CharField(source='user_account.name')
    category = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'date', 'user',
                  'user_account', 'category', 'description']

    def get_category(self, obj):
        return {
            'name': obj.category.name,
            'type': obj.category.type
        }


class TransactionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount', 'date', 'user_account', 'category', 'description']

    def validate(self, data):
        user = self.context['request'].user
        account = data['user_account']
        category = data['category']

        if account.user != user:
            raise ValidationError(
                {'user_account': 'The account does not belong to the user'})

        if category.user and user != category.user:
            raise ValidationError(
                {'category': 'The category is not a default category or does not belong to the user'})

        return data


class TransferDetailSerializer(serializers.ModelSerializer):
    user = serializers.EmailField(source='user.email', read_only=True)
    from_user_account = serializers.CharField(source='from_user_account.name')
    to_user_account = serializers.CharField(source='to_user_account.name')

    class Meta:
        model = Transfer
        fields = ['id', 'date', 'amount', 'user',
                  'from_user_account', 'to_user_account', 'description']


class TransferCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['amount', 'date', 'from_user_account',
                  'to_user_account', 'description']

    def validate(self, data):
        user = self.context['request'].user
        from_user_account = data['from_user_account']
        to_user_account = data['to_user_account']

        if user != from_user_account.user or user != to_user_account.user:
            raise ValidationError(
                "The accounts involved do not belong to the user")

        if from_user_account == to_user_account:
            raise ValidationError(
                "The accounts involved are the same")

        return data
