from django.db import models

# Create your models here.
class Item(models.Model):
    CATEGORY_CHOICES = [
        ('fruit','과일'),
        ('seed','모종'),
        
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    price_per_small = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    price_per_big = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return self.name