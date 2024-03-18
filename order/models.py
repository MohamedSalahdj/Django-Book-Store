from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MinLengthValidator




class OrderStatus(models.TextChoices):
    PENDING = 'Pending'
    COMPLETED = 'Completed'
    CANCELLED= 'Cancelled'

class Orderlist(models.Model):

    # user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # book = models.ForeignKey(book, null=True, on_delete=models.SET_NULL)
    book_name = models.CharField(max_length=20, validators=[MinLengthValidator(3)])
    price = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1)])
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    order_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='orderdbooks',default='default.png') 
    status = models.CharField(max_length=60, choices=OrderStatus.choices, default=OrderStatus.PENDING)
   



    @property
    def total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return self.book_name
        






     