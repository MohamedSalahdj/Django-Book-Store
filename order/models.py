from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MinLengthValidator
from users.models import CustomUser
from book.models import Book

class OrderStatus(models.TextChoices):
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    ordered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])  
    is_orderd = models.BooleanField(default=False)

    class Meta:
        ordering = ['-ordered_date']

    def __str__(self):
        return f"Order {self.id} by {self.user.first_name}"  


class OrderItem(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])   
    
    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.book.name}  ({self.quantity})"

