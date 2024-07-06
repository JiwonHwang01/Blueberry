from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    CATEGORY_CHOICES = [
        ('fruit','Fruit'),
        ('seed','Seed'),
        
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    price_per_small = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_per_big = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    SIZE_CHOICES = [
        ('small', 'Small'),
        ('big', 'Big'),
    ]
    
    STATUS_CHOICES = [
        ('pending', '입금확인중'),
        ('preparing', '배송준비중'),
        ('shipping', '배송중'),
        ('completed', '배송완료'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.TextField()
    preferred_delivery_date = models.DateField()
    depositor_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        if self.item.category == 'fruit':
            if self.size == 'small':
                self.total_price = self.quantity * self.item.price_per_small
            elif self.size == 'big':
                self.total_price = self.quantity * self.item.price_per_big
        else:
            self.total_price = self.quantity * self.item.price_per_unit
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} - {self.item.name} - {self.status}'