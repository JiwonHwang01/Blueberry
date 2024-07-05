from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from django.contrib.auth.password_validation import (
    UserAttributeSimilarityValidator as BaseUserAttributeSimilarityValidator,
    MinimumLengthValidator as BaseMinimumLengthValidator,
    CommonPasswordValidator as BaseCommonPasswordValidator,
    NumericPasswordValidator as BaseNumericPasswordValidator,
)
class UserAttributeSimilarityValidator(BaseUserAttributeSimilarityValidator):
    def __init__(self, user_attributes=None, max_similarity=0.7, message=None):
        self.user_attributes = user_attributes or ['username', 'email', 'first_name', 'last_name']
        self.max_similarity = max_similarity
        self.message = message or _('비밀번호가 사용자 정보와 너무 유사합니다.')

    def validate(self, password, user=None):
        super().validate(password, user)
        raise ValidationError(self.message, code='password_too_similar')
    
class MinimumLengthValidator(BaseMinimumLengthValidator):
    def __init__(self, min_length=8, message=None):
        self.min_length = min_length
        self.message = message or _('비밀번호는 최소 %(min_length)d자 이상이어야 합니다.') % {'min_length': self.min_length}

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(self.message, code='password_too_short')
        
class CommonPasswordValidator(BaseCommonPasswordValidator):
    def __init__(self, message=None):
        self.message = message or _('비밀번호가 너무 흔합니다. 다른 비밀번호를 사용하세요.')

    def validate(self, password, user=None):
        super().validate(password, user)
        raise ValidationError(self.message, code='password_too_common')

class NumericPasswordValidator(BaseNumericPasswordValidator):
    def __init__(self, message=None):
        self.message = message or _('비밀번호에 숫자 외에 문자를 포함해주세요.')

    def validate(self, password, user=None):
        super().validate(password, user)
        raise ValidationError(self.message, code='password_entirely_numeric')