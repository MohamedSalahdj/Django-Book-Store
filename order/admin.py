from django.contrib import admin
from .models import Order,OrderItem, Cart, CartIetm
# Register your models here.




class OrderAdmin(admin.ModelAdmin):
   
    list_display = ['id', 'user', 'ordered_date', 'status', 'is_orderd']
    
    
   
    

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['book', 'order', 'price', 'quantity', 'total_price']

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Cart)
admin.site.register(CartIetm)
