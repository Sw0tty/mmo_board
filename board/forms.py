from collections.abc import Mapping
from typing import Any
from django.contrib.auth.models import Group, User
from allauth.account.forms import SignupForm
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from board.models import Advertisement


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user


class CreatingAdvertisementForm(forms.ModelForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Наименование'
        self.fields['description'].label = 'Описание'
        self.fields['category'].label = 'Категория'
        self.fields['category'].empty_label = 'Выберите категорию'
    
    class Meta:
        model = Advertisement

        fields = [
            'title',
            'description',
            'category',
        ]


class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Наименование'
        self.fields['description'].label = 'Описание'
        self.fields['category'].label = 'Категория'
        self.fields['author'].label = 'Автор'
        self.fields['author'].disabled = True

    class Meta:
        model = Advertisement

        fields = [
            'title',
            'description',
            'category',
            'author'
        ]


class CreatingReplyForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['description'].label = 'Описание'
    
    class Meta:
        model = Advertisement

        fields = [
            'description',
        ]