from django.urls import path
from .views import create_order, order_success
from . import views

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('success/', order_success, name='order_success'),
]