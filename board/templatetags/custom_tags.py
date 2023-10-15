from django import template
from random import choice
from board.models import Advertisement

register = template.Library()


@register.simple_tag()
def random_new_id():
    return choice([i['id'] for i in Advertisement.objects.all().values('id')])
