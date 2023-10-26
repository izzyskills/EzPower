from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import CustomUser, Transaction, Account, Token, Meter


@receiver(post_save, sender=CustomUser)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)
        Meter.objects.create(user=instance, location=instance.address, unit=0)


@receiver(pre_save, sender=Transaction)
def generate_token(sender, instance, **kwargs):
    if not instance.token_id:
        user = instance.account.user
        meter = Meter.objects.get(user=user)
        instance.token = Token.objects.create(unit=instance.amount / 450, meter=meter)
