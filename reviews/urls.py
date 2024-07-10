from django.urls import path
from .views import review_list, review_create

urlpatterns = [
    path('', review_list, name='review_list'),
    path('create/', review_create, name='review_create'),
]