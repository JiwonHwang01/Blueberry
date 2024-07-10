from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['item', 'size', 'comment', 'image']
        labels = {
            'item': '상품',
            'size': '과일 크기',
            'comment': '코멘트',
            'image': '이미지',
        }