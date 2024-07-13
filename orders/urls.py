from django.urls import path
from .views import create_order, order_success, order_list
from . import views

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('success/', order_success, name='order_success'),
    path('list/', order_list, name='order_list'),
    path('info/', views.info, name='info'),
]