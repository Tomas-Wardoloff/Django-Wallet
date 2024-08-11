from rest_framework import serializers

from .models import Transaction, Transfer


class TransactionSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()
    account_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    type = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = ['id',  'user_email', 'amount', 'date',
                  'account_name', 'category_name', 'type', 'description']

    def get_user_email(self, obj):
        return obj.user.email

    def get_account_name(self, obj):
        return obj.user_account.name

    def get_category_name(self, obj):
        return obj.category.name

    def get_type(self, obj):
        return obj.category.type

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
