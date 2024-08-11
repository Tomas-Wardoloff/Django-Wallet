from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Transaction, Transfer


@receiver(post_save, sender=Transaction)
def update_account_balance_income_created(sender, instance, created, **kwargs):
    if created:
        if instance.category.type == 'Income':
            instance.user_account.update_balance(instance.amount)
        else:
            instance.user_account.update_balance(-instance.amount)


@receiver(post_delete, sender=Transaction)
def update_account_balance_income_deleted(sender, instance, **kwargs):
    if instance.category.type == 'Income':
        instance.user_account.update_balance(-instance.amount)
    else:
        instance.user_account.update_balance(instance.amount)


@receiver(post_save, sender=Transfer)
def update_account_balance_transfer_created(sender, instance, created, **kwargs):
    if created:
        instance.from_user_account.update_balance(-instance.amount)
        instance.to_user_account.update_balance(instance.amount)


@receiver(post_delete, sender=Transfer)
def update_account_balance_transfer_deleted(sender, instance, **kwargs):
    instance.from_user_account.update_balance(instance.amount)
    instance.to_user_account.update_balance(-instance.amount)
