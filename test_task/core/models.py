from django.db import models
from django.core.exceptions import ValidationError



def validate_count(value):
    if value < 0:
        raise ValidationError("Count must not be negative!")


class Product(models.Model):
    name = models.CharField(max_length=100)
    decription = models.CharField(max_length=200)
    count = models.IntegerField(validators=[validate_count])
    delivery_date = models.DateField(auto_now_add=True)
    expiry_date = models.DateField()

    def save(self, *args, **kwargs):
        self.clean_fields()
        self.validate_expiry_date()
        super().save(*args, **kwargs)

    def validate_expiry_date(self):
        if self.expiry_date <= self.delivery_date:
            raise ValidationError("Expiry date must be greater than delivery date!")

