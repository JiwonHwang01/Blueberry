from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': '사용자 이름',
        }
        help_texts = {
            'username': '사용자 이름은 고유해야 합니다.',
            'password1': '비밀번호는 최소 8자 이상이어야 하며, 흔하지 않아야 합니다.',
            'password2': '비밀번호를 한 번 더 입력하여 확인하세요.',
        }
        error_messages = {
            'username': {
                'unique': '이미 사용 중인 사용자 이름입니다. 다른 이름을 사용해 주세요.',
            },
            
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 비밀번호 관련 필드에 도움말 추가
        self.fields['password1'].label = '비밀번호'
        self.fields['password2'].label = '비밀번호 확인'
        self.fields['password2'].help_text = ''
        self.fields['password1'].help_text = '비밀번호는 최소 8자 이상이어야 합니다.'
        