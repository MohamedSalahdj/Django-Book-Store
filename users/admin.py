from django.contrib import admin
from .models import CustomUser, CustomPublisher
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CustomPublisher)