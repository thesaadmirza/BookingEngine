import datetime
from django.core.exceptions import ValidationError


def validate_day(day):
    today = datetime.date.today()
    if day < today:
        raise ValidationError('Blocked Date cannot be in the Past.')
