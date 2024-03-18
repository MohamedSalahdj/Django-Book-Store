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
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)
    is_ordered = models.BooleanField()

    def __str__(self):
        return 'User: ' + self.user.first_name + ' ' + self.user.last_name + ', Order Id: ' + str(self.id)

class OrderItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orderitems')
    # book_name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    # book_image = models.ImageField(upload_to='orderdbooks', default='default.png') 
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    status = models.CharField(max_length=60, choices=OrderStatus.choices, default=OrderStatus.PENDING)

    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return self.book_name