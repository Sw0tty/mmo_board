from django import template
from board.models import Advertisement, Reply


register = template.Library()


@register.filter()
def get_no_adopted_replies_count(model_id):
    return (Reply.objects.filter(advertisement_id__id=model_id, adopted=False)).count()


@register.filter()
def get_replies_count(model_id, arg=True):
    return (Reply.objects.filter(advertisement_id__id=model_id, adopted=arg)).count()
