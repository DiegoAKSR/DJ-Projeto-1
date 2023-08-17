import re

from django.core.exceptions import ValidationError


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    field.widget.attrs['placeholder'] = placeholder_val


def strong_password(password):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        if len(password) < 8:
            raise ValidationError(
                'Senha Fraca: Precisa conter no mínimo 8 digitos.')
        else:
            raise ValidationError(
                'Senha Fraca: Precisa conter letras Maiúsculas, Minúsculas e Números.')
