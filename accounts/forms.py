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
            'password1': {
            'required': '비밀번호를 입력해 주세요.',
            'min_length': '비밀번호는 최소 8자 이상이어야 합니다.',
            'password_mismatch': '비밀번호가 일치하지 않습니다.',
            'too_common': '비밀번호가 너무 흔합니다. 더 강력한 비밀번호를 사용하세요.',
            'too_short': '비밀번호가 너무 짧습니다. 8자 이상으로 입력하세요.',
            'common_password': '비밀번호가 너무 흔합니다. 다른 비밀번호를 사용하세요.',
            'password_validation_failed': '비밀번호 검증에 실패했습니다. 유효한 비밀번호를 입력하세요.',
            }
            
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 비밀번호 관련 필드에 도움말 추가
        self.fields['password1'].label = '비밀번호'
        self.fields['password2'].label = '비밀번호 확인'
        self.fields['password2'].help_text = ''
        self.fields['password1'].help_text = '비밀번호는 최소 8자 이상이어야 합니다.'
        