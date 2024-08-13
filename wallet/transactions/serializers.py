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


class TransferSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    account_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    from_account = serializers.SerializerMethodField()
    to_account = serializers.SerializerMethodField()

    class Meta:
        model = Transfer
        fields = ['id',  'user_email', 'amount', 'date',
                  'from_account', 'to_account', 'category_name', 'description']

    def get_user_email(self, obj):
        return obj.user.email

    def get_account_name(self, obj):
        return obj.user_account.name

    def get_category_name(self, obj):
        return obj.category.name

    def get_from_account(self, obj):
        return obj.from_user_account.name

    def get_to_account(self, obj):
        return obj.to_user_account.name
