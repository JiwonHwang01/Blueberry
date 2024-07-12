from django.contrib import admin
from .models import Item

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price_per_small', 'price_per_big', 'price_per_unit']
    list_filter = ['category']
    search_fields = ['name']
