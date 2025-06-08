from django.db import migrations
from django.utils.crypto import get_random_string
from datetime import datetime

def generate_order_numbers(apps, schema_editor):
    Order = apps.get_model('orders', 'Order')
    for order in Order.objects.all():
        if not order.order_number:
            date_str = order.created_at.strftime('%Y%m%d') if order.created_at else datetime.now().strftime('%Y%m%d')
            random_num = get_random_string(4, allowed_chars='0123456789')
            order_number = f"{date_str}{random_num}"
            while Order.objects.filter(order_number=order_number).exists():
                random_num = get_random_string(4, allowed_chars='0123456789')
                order_number = f"{date_str}{random_num}"
            order.order_number = order_number
            order.save()

class Migration(migrations.Migration):
    dependencies = [
        ('orders', '0009_order_created_at'),
    ]
    operations = [
        migrations.RunPython(generate_order_numbers),
    ] 