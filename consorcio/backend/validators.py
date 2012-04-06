from django.core.exceptions import ValidationError

def validate_not_empty_string(value):
    if value == '':
        raise ValidationError("string should not be empty")
