from django.contrib import admin
from .models import Orderlist
# Register your models here.

class OrderlistAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'price', 'quantity', 'total_price', 'order_date']


admin.site.register(Orderlist,OrderlistAdmin)