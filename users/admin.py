from django.contrib import admin
from .models import CustomUser, CustomPublisher, Address
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CustomPublisher)
admin.site.register(Address)
