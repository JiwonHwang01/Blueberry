from django.db import models
from django.contrib.auth.models import User
from orders.models import Item

# Create your models here.
class Review(models.Model):
    SIZE_CHOICES = [
        ('small', '소과'),
        ('big', '대과'),
        ('none', '해당 없음(모종)')
    ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.item.name}"