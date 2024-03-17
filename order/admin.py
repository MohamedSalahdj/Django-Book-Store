from django.contrib import admin
from .models import Orderlist
# Register your models here.

class OrderlistAdmin(admin.ModelAdmin):
    list_display = ['id','book_name', 'price', 'quantity', 'total_price', 'order_date','image']


admin.site.register(Orderlist,OrderlistAdmin)