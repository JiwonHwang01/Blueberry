# admin/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('items/', views.item_list, name='admin_item_list'),
    path('items/create/', views.create_item, name='create_item'),
    path('items/<int:item_id>/edit/', views.edit_item, name='edit_item'),
    path('items/<int:item_id>/delete/', views.delete_item, name='delete_item'),
    path('orders/', views.order_list, name='admin_order_list'),
    path('orders/<int:order_id>/update_status/', views.update_order_status, name='update_order_status'),
]