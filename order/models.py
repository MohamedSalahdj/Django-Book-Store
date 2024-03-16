from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MinLengthValidator


class Orderlist(models.Model):
 
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    book_name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    order_date = models.DateField()
    image = models.ImageField(upload_to='orderdbooks',default='default.png') 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return self.book_name
        