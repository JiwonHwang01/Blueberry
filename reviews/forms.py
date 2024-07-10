from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['item', 'rating', 'comment', 'image']
        labels = {
            'item': '상품',
            'rating': '평점',
            'comment': '코멘트',
            'image': '이미지',
        }