from datetime import date

from django.core.exceptions import ValidationError


def age_verification(value: date):
    quantity_days = date.today().year * 365 + date.today().month * 30 + date.today().day \
                    - value.year * 365 - value.month * 30 - value.day
    quantity_years = quantity_days / 365
    if quantity_years < 9:
        raise ValidationError(
            "Access denied",
            params={'value': value}
        )


def mail_verification(value):
    if 'rambler.ru' in value:
        raise ValidationError(
            f"Регистрация с почты rambler.ru запрещена",
            params={'value', value}
        )
