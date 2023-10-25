from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import CustomUser, Transaction, Account, Token


@receiver(post_save, sender=CustomUser)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)


@receiver(pre_save, sender=Transaction)
def generate_token(sender, instance, **kwargs):
    if not instance.token_id:
        instance.token = Token.objects.create(unit=instance.amount / 450)
