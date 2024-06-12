from django.core.exceptions import ValidationError


def validate_numeric(value):
    if not value.isdigit():
        raise ValidationError(
            '%(value)s only contains digits',
            params={'value': value},
        )