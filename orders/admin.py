from django.contrib import admin
from .models import Item, Order

# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'item', 'size', 'quantity', 'total_price', 'status', 'preferred_delivery_date']
    list_filter = ['status', 'preferred_delivery_date']
    search_fields = ['user__username', 'item__name', 'name', 'contact', 'address', 'depositor_name']
