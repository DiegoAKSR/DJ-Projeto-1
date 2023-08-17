from django import forms

from utils.django_forms import add_placeholder


class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Digite seu Usuario')
        add_placeholder(self.fields['password'], 'Digite sua Senha')

    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
