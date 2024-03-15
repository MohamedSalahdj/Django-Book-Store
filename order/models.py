from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MinLengthValidator


class Orderlist(models.Model):
 

    book_name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    order_date = models.DateField()


    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return self.book_name
        