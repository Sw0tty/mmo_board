from django import template
from random import choice
from board.models import Advertisement
from django.urls import reverse_lazy

register = template.Library()


@register.simple_tag()
def random_advertisement_id():
    try:
        return choice([i['id'] for i in Advertisement.objects.all().values('id')])
    except IndexError:
        return ''
