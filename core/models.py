from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from .utility import Random11digit


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
    account_id = Random11digit()
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} {self.account_id}"


class Meter(models.Model):
    meter_id = Random11digit()
    location = models.CharField(max_length=50)
    unit = models.DecimalField(max_digits=9, decimal_places=2)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)


class Token(models.Model):
    token_id = Random11digit()
    unit = models.DecimalField(max_digits=9, decimal_places=2)
    used = models.BooleanField(default=False)
    meter = models.ForeignKey(Meter, on_delete=models.CASCADE)


class Transaction(models.Model):
    transaction_id = Random11digit()
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    token = models.OneToOneField(Token, on_delete=models.CASCADE)
