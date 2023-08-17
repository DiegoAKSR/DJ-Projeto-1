
from unittest import TestCase

from django.test import TestCase as DjangoTestcase
from django.urls import reverse
from parameterized import parameterized

from authors.forms import RegisterForm


class AuthorRegisterForUnitTest(TestCase):
    @parameterized.expand([
        ('first_name', 'Digite seu Nome'),
        ('last_name', 'Digite seu Sobrenome'),
        ('username', 'Digite seu Nick/Usuario'),
        ('email', 'Digite seu E-mail'),
        ('password', 'Digite sua Senha'),
        ('password2', 'Repita sua Senha'),
    ])
    def test_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        placeholder_field = form[field].field.widget.attrs['placeholder']
        self.assertEqual(placeholder, placeholder_field)


class AuthorRegisterForIntegrationTest(DjangoTestcase):
    def setUp(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@anymal.com',
            'password': 'str0ngP@ssword1',
            'password2': 'str0ngP@ssword1',
        }
        return super().setUp(*args, **kwargs)

    @parameterized.expand([
        ('username', 'Este campo é obrigatório.'),
        ('first_name', 'Digite seu Nome'),
        ('last_name', 'Digite seu Sobrenome'),
        ('password', 'Este campo é obrigatório.'),
        ('password2', 'Repita sua senha'),
        ('email', 'E-mail Obrigatorio.'),
    ])
    def test_fields_cannot_be_empty(self, field, msg):
        self.form_data[field] = ''
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get(field))

    def test_username_field_min_lenght_should_be_4(self):
        self.form_data['username'] = 'oo'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Certifique-se de que o valor tenha no mínimo 5 caracteres (ele possui 2).'
        self.assertIn(msg, response.content.decode('utf-8'))
        self.assertIn(msg, response.context['form'].errors.get('username'))

    def test_username_field_max_lenght_should_be_150(self):
        self.form_data['username'] = 'o' * 155
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Certifique-se de que o valor tenha no máximo 150 caracteres (ele possui 155).'

        self.assertIn(msg, response.context['form'].errors.get('username'))
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_password_field_have_lower_upper_case_letters_And_numbers(self):
        self.form_data['password'] = 'aa'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'Senha Fraca: Precisa conter no mínimo 8 digitos.'

        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_password_and_password_confirmation_are_equal(self):
        self.form_data['password'] = 'asdF12345'
        self.form_data['password2'] = 'asdF123456'
        url = reverse('authors:create')
        response = self.client.post(url, data=self.form_data, follow=True)
        msg = 'As senhas  sao diferentes'

        self.assertIn(msg, response.context['form'].errors.get('password'))
        self.assertIn(msg, response.content.decode('utf-8'))

    def test_send_get_request_to_registration_create_view_returns_404(self):

        url = reverse('authors:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_author_created_can_login(self):
        url = reverse('authors:create')

        self.form_data.update({
            'username': 'testuser',
            'password': '@12345aD',
            'password2': '@12345aD',
        })

        self.client.post(url, data=self.form_data, follow=True)

        is_autenticated = self.client.login(
            username='testuser',
            password='@12345aD',
        )

        self.assertTrue(is_autenticated)
