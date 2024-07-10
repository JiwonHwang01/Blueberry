from django.test import TestCase
from django.contrib.auth.models import User
from .models import Item, Order
from django.urls import reverse
from datetime import date, timedelta

# Create your tests here.
class OrderTestCase(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create items
        self.item1 = Item.objects.create(
            name='Apple', 
            category='fruit', 
            price_per_small=3, 
            price_per_big=5
        )
        
        self.item2 = Item.objects.create(
            name='Banana', 
            category='fruit', 
            price_per_small=5, 
            price_per_big=8
        )
        
        # Login the user
        self.client.login(username='testuser', password='password')

    def test_order_creation(self):
        response = self.client.post(reverse('create_order'), {
            'item': self.item1.id,
            'size': 'small',
            'quantity': 10,
            'name': 'Hwang',
            'contact': '01012345678',
            'postcode': '16000',
            'address': '우리집',
            'extra_address': '',
            'detail_address': '1605',
            'preferred_delivery_date': date.today() + timedelta(days=3),
            'depositor_name': 'Hwang',
        })
        
        self.assertEqual(response.status_code, 302)  # Redirect after successful creation
        
        order = Order.objects.get(user=self.user)
        self.assertEqual(order.total_price, 30)  # 10 * 3

    def test_order_list_view(self):
        Order.objects.create(
            user=self.user,
            item=self.item1,
            size='small',
            quantity=5,
            name='Hwang',
            contact='01012345678',
            postcode='16000',
            address='우리집',
            extra_address='',
            detail_address='1605',
            preferred_delivery_date=date.today() + timedelta(days=3),
            depositor_name='Hwang',
            status='pending',
            total_price=15
        )
        
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Apple')
        self.assertContains(response, '소과')
        self.assertContains(response, '5원')

    def test_order_total_price_calculation(self):
        order = Order.objects.create(
            user=self.user,
            item=self.item2,
            size='big',
            quantity=10,
            name='Hwang',
            contact='',
            postcode='',
            address='',
            extra_address='',
            detail_address='',
            preferred_delivery_date=date.today() + timedelta(days=5),
            depositor_name='Hwang',
            status='pending',
            total_price=0  # 아래 save에 계산될 거임
        )
        
        order.save()
        self.assertEqual(order.total_price, 80)  # 10 * 8