from collections import defaultdict
from typing import Any

from django import forms
from django.core.exceptions import ValidationError

from news.models import New
from utils.django_forms import add_attr


class AuthorNewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

        add_attr(self.fields.get('text_post'), 'class', 'span-2')

    class Meta:
        model = New
        fields = ('title', 'description', 'text_post', 'cover', 'category')
        widgets = {
            'cover': forms.FileInput(
                attrs={'class': 'span-2'})}\


    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)

        cd = self.cleaned_data
        title = cd.get('title')
        description = cd.get('description')
        category = cd.get('category')

        if len(title) < 5:
            self._my_errors['title'].append(
                'O titulo precisa conter 5  ou mais caracteres.'
            )

        if len(description) < 5:
            self._my_errors['description'].append(
                'A descrição precisa conter 5  ou mais caracteres.'
            )

        if category is None:
            self._my_errors['category'].append(
                'Selecione uma categoria.'
            )

        if self._my_errors:
            raise ValidationError(self._my_errors)

        return super_clean
