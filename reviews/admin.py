from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display= ['item', 'size', 'user', 'comment', 'image', 'created_at']
    list_filter = ['created_at']
    search_fields=['item__category', 'size', 'user__username']