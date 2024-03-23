from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MinLengthValidator
from django.utils import timezone
from users.models import CustomUser, CustomPublisher
from book.models import Book
from users.models import Address
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField


# class OrderStatus(models.TextChoices):
#     PENDING   = 'Pending'
#     COMPLETED = 'Completed'
#     CANCELLED = 'Cancelled'

order_status = (
    ('Received', 'Received'),
    ('Processed', 'Processed'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered')
)
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders')
    ordered_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=order_status)
    # quantity = models.IntegerField(validators=[MinValueValidator(1)])  
    total = models.FloatField()
    is_orderd = models.BooleanField(default=False)
    delivery_address = models.ForeignKey(Address, on_delete=models.SET_NULL, related_name='delivery_order_address', null=True, blank=True)
    # delivery_time =
    # is_payment = 

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
    total = models.FloatField(null=True,blank=True)

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

    @property
    def cart_total(self):
        total = 0
        for item in self.cart_items.all():
            if item.total is not None:
                total += item.total
        return round(total,2)

    def __str__(self):
        return str(self.customer.first_name).capitalize() + ' ' + str(self.customer.last_name).capitalize()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    publisher = models.ForeignKey(CustomPublisher, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='cart_item_book')
    quantity = models.IntegerField(default=1)
    total = models.FloatField(null=True, blank=True)



class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payment_order')
    card_number = CardNumberField(blank=True)
    expire = CardExpiryField(blank=True)
    security_code = SecurityCodeField(blank=True)
