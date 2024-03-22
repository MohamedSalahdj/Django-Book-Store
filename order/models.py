from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MinLengthValidator
from django.utils import timezone
from users.models import CustomUser, CustomPublisher
from book.models import Book

class OrderStatus(models.TextChoices):
    PENDING   = 'Pending'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    ordered_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])  
    is_orderd = models.BooleanField(default=False)
    # delivery_time = 

    class Meta:
        ordering = ['-ordered_date']

    def __str__(self):
        return f"Order {self.id} by {self.user.first_name}"  


class OrderItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='order_book_item')
    publisher = models.ForeignKey(CustomPublisher, on_delete=models.CASCADE, related_name='order_publisher_item')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])   
    
    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.book.name}  ({self.quantity})"


cart_sataus = (
    ('InProgress', 'InProgress'),
    ('Completed', 'Completed')

)

class Cart(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='carts')
    status = models.CharField(max_length=10, choices=cart_sataus)

    def __str__(self):
        return str(self.customer.first_name).capitalize() + ' ' + str(self.customer.last_name).capitalize()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    publisher = models.ForeignKey(CustomPublisher, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='cart_item_book')
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True, blank=True)
