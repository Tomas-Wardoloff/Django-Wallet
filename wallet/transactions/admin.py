from django.contrib import admin

from .models import Transaction, Transfer


class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_filter = ['date', 'category', 'user', 'user_account']
    list_display = ['amount', 'date', 'category', 'type', 'user', 'user_account_name']

    def user_account_name(self, obj) -> str:
        return obj.user_account.name
    
    def type(self, obj) -> str:
        return obj.category.type


class TransferAmind(admin.ModelAdmin):
    model = Transfer
    list_filter = ['date', 'category', 'user', 'user_account']
    list_display = ['amount', 'date', 'category', 'user',
                    'from_user_account_name', 'to_user_account_name']

    def from_user_account_name(self, obj) -> str:
        return obj.from_user_account.name

    def to_user_account_name(self, obj) -> str:
        return obj.to_user_account.name


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Transfer)
