from django.urls import path
from .views import create_order, order_success, order_list
from . import views

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('success/', order_success, name='order_success'),
    path('list/', order_list, name='order_list'),
    path('info/', views.info, name='info'),
    path('request-cancel/<str:order_number>/', views.request_cancel, name='request_cancel'),
    path('complete-order/<str:order_number>/', views.complete_order, name='complete_order'),
    path('detail/<str:order_number>/', views.order_detail, name='order_detail'),
]