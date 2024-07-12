from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'price_per_small', 'price_per_big', 'price_per_unit']
        labels = {
            'name': '상품명',
            'category': '카테고리',
            'price_per_small': '소형 가격',
            'price_per_big': '대형 가격',
            'price_per_unit': '단위 가격',
        }