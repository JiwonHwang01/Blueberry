# Generated by Django 4.2.13 on 2024-07-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_item_delete_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cancel_requested',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', '입금확인중'), ('preparing', '배송준비중'), ('shipping', '배송중'), ('completed', '배송완료'), ('canceling', '취소요청'), ('cancelled', '취소완료')], default='입금확인중', max_length=10),
        ),
    ]
