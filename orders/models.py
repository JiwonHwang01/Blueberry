from django.db import models
from django.contrib.auth.models import User
from items.models import Item

# Create your models here.
class Order(models.Model):
    SIZE_CHOICES = [
        ('small', '소과'),
        ('big', '대과'),
        ('none', '모종(해당없음)'),
    ]
    
    STATUS_CHOICES = [
        ('pending', '입금확인중'),
        ('preparing', '배송준비중'),
        ('shipping', '배송중'),
        ('completed', '배송완료'),
        ('canceling', '취소요청'),
        ('cancelled', '취소완료'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES, null=True, blank=True)
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    detail_address = models.CharField(max_length=255)
    preferred_delivery_date = models.DateField()
    depositor_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='입금확인중')
    review_written = models.BooleanField(default=False) #TODO
    total_price = models.DecimalField(max_digits=10, decimal_places=0, editable=False)
    cancel_requested = models.BooleanField(default=True)

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