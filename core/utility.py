from django.db import models as md
from django.core.exceptions import ValidationError
import random
from . import models


class Random11digit(md.IntegerField):
    """this inherits all the attributes of the integer field and
    generates a random primary key for the models
    its being utilized due to the data requirement stated in the ERD."""

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
                not models.Account.objects.filter(account_id=value).exists()
                and not models.Transaction.objects.filter(transaction_id=value).exists()
                and not models.Token.objects.filter(token_id=value).exists()
                and not models.Meter.objects.filter(meter_id=value).exists()
            ):
                return value

    def validate_11_digit_integer(self, value):
        if not (100_000_000_00 <= value <= 999_999_999_99):
            raise ValidationError("Value must be an 11-digit integer.")


def use_token(pk):
    token = models.Token.objects.get(token_id=pk)
    if token.used == False:
        token.meter.unit += token.unit
        token.save()
