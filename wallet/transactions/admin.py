from django.contrib import admin

from .models import Income, Expense, Transfer


class IncomeAdmin(admin.ModelAdmin):
    model = Income
    list_filter = ['date', 'category', 'user', 'user_account']
    list_display = ['amount', 'date', 'category', 'user', 'user_account_name']

    def user_account_name(self, obj) -> str:
        return obj.user_account.name


class ExpenseAdmin(admin.ModelAdmin):
    model = Expense
    list_filter = ['date', 'category', 'user', 'user_account']
    list_display = ['amount', 'date', 'category', 'user', 'user_account_name']

    def user_account_name(self, obj) -> str:
        return obj.user_account.name


class TransferAmind(admin.ModelAdmin):
    model = Transfer
    list_filter = ['date', 'category', 'user', 'user_account']
    list_display = ['amount', 'date', 'category', 'user',
                    'from_user_account_name', 'to_user_account_name']

    def from_user_account_name(self, obj) -> str:
        return obj.from_user_account.name

    def to_user_account_name(self, obj) -> str:
        return obj.to_user_account.name


admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Transfer)
