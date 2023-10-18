from django import template
from random import choice
from django.shortcuts import render
from board.models import Advertisement, Reply
from django.urls import reverse_lazy

register = template.Library()


@register.simple_tag()
def random_advertisement_id():
    try:
        return choice([i['id'] for i in Advertisement.objects.all().values('id')])
    except IndexError:
        return ''


@register.simple_tag()
def get_replies_count():
    context = {
        'replies': Reply.objects.all()
    }
    return context
