import re
from typing import Any, Dict

from django import forms
from django.contrib.auth.models import User
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


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        add_placeholder(self.fields['first_name'], 'Digite seu Nome')
        add_placeholder(self.fields['last_name'], 'Digite seu Sobrenome')
        add_placeholder(self.fields['username'], 'Digite seu Nick/Usuario')
        add_placeholder(self.fields['email'], 'Digite seu E-mail')
        add_placeholder(self.fields['password'], 'Digite sua Senha')
        add_placeholder(self.fields['password2'], 'Repita sua Senha')

    username = forms.CharField(
        label='Nome de Usuario',
        help_text=(
            'Deve conter entre 5 e 150 caracteres, podendo ser, letras, numeros ou simbolos.'),
        min_length=5, max_length=150
    )

    first_name = forms.CharField(
        error_messages={'required': 'Digite seu Nome'},
        label='Nome'
    )

    last_name = forms.CharField(
        error_messages={'required': 'Digite seu Sobrenome'},
        label='Sobrenome'
    )

    email = forms.EmailField(
        error_messages={'required': 'E-mail Obrigatorio.'},
    )

    password2 = forms.CharField(
        required=True,
        label='Confirmar Senha',
        widget=forms.PasswordInput(),
        error_messages={'required': 'Repita sua senha'},

    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[strong_password],
        help_text='A Senha deve conter letras Maiúsculas, Minúsculas e Números.',
        label='Senha'
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if not password == password2:
            raise ValidationError({'password': 'As senhas  sao diferentes'})
