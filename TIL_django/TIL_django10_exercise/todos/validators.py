from django.core.exceptions import ValidationError

def first_validator(value):
    if ("@" in value) or ("@" in value):
        raise ValidationError("'@' 와 '#'은 내용에 포함될 수 없습니다.", code='symbol-err')


