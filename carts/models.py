# from django.db import models
# from book.models import Book
# from users.models import CustomUser

# # Create your models here.

# class Cart(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     Book = models.ManyToManyField(Book, through='CartItem')

#     def __str__(self):
#         return f"Cart " + str(self.id) + " for " + self.user.email


# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
#     Book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0)

#     def __str__(self):
#         return self.product.name 
