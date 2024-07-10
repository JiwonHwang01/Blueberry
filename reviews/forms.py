from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['item', 'size', 'comment', 'image']
        labels = {
            'item': '상품',
            'size': '과일 크기',
            'comment': '내용',
            'image': '이미지',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item'].widget = forms.HiddenInput()
        self.fields['size'].widget = forms.HiddenInput()