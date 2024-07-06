from django import forms
from .models import Order,Item

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'item', 'size', 'quantity', 'name', 'contact', 'address',
            'preferred_delivery_date', 'depositor_name'
        ]
        labels = {
            'item': '상품', 
            'size': '크기', 
            'quantity' : '수량', 
            'name' : '이름', 
            'contact' : '연락처', 
            'address' : '주소',
            'preferred_delivery_date' : '배송희망일', 
            'depositor_name' : '입금자명',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['size'].required = False

        if self.instance.pk and self.instance.item:
            if self.instance.item.category == 'fruit':
                self.fields['size'].required = True
                self.fields['size'].widget.attrs['style'] = 'display:block;'
            else:
                self.fields['size'].widget.attrs['style'] = 'display:none;'