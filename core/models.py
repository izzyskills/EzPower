from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.exceptions import ValidationError
import random

# -- >  what the fuck is this for ? 

class Custom11DigitIntegerField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs["primary_key"] = True
        kwargs["default"] = self.generate_unique_11_digit_integer
        kwargs["unique"] = True
        kwargs["validators"] = [self.validate_11_digit_integer]
        super().__init__(*args, **kwargs)

    def generate_unique_11_digit_integer(self):
        while True:
            value = random.randint(100_000_000_00, 999_999_999_99)
            if (
                not Account.objects.filter(account_id=value).exists()
                and not Transaction.objects.filter(transaction_id=value).exists()
                and not Token.objects.filter(token_id=value).exists()
                and not Meter.objects.filter(meter_id=value).exists()
            ):
                return value

    def validate_11_digit_integer(self, value):
        if not (100_000_000_00 <= value <= 999_999_999_99):
            raise ValidationError("Value must be an 11-digit integer.")


class CustomUserManager(BaseUserManager):
    def create_user(
        self, username, address, phone_number, password=None, **extra_fields
    ):
        if not username:
            raise ValueError("The username field must be set")
        user = self.model(
            username=username,
            address=address,
            phone_number=phone_number,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, address, phone_number, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(
            username, address, phone_number, password, **extra_fields
        )


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=15, unique=True, db_index=True)
    address = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["address", "phone_number"]

    def __str__(self):
        return self.username


# Create your models here.
class Account(models.Model):
    account_id = Custom11DigitIntegerField()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} {self.account_id}"


class Meter(models.Model):
    meter_id = Custom11DigitIntegerField()
    location = models.CharField(max_length=50)
    unit = models.DecimalField(max_digits=9, decimal_places=2)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)


class Token(models.Model):
    token_id = Custom11DigitIntegerField()
    unit = models.DecimalField(max_digits=9, decimal_places=2)
    used = models.BooleanField(default=False)
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)


class Transaction(models.Model):
    transaction_id = Custom11DigitIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    token = models.OneToOneField(Token, on_delete=models.CASCADE)
