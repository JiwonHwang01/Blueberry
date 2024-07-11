from django import forms
from .models import Review, Item

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

class ReviewFilterForm(forms.Form):
    item = forms.ModelChoiceField(queryset=Item.objects.all(), required=False, label="품목")
    size = forms.ChoiceField(choices=[('', '크기 선택'), ('small', '소과'), ('big', '대과')], required=False, label="크기")
    month = forms.ChoiceField(choices=[('', '월 선택')] + [(str(i), f'{i}월') for i in range(1, 13)], required=False, label='월')