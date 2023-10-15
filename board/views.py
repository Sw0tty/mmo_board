from django.shortcuts import render
from django.views.generic import ListView, DetailView
from board.models import Advertisement


class AdvertisementsList(ListView):
    model = Advertisement
    template_name = 'advertisements_list.html'
    context_object_name = 'advertisements'
    ordering = 'datetime_in'
    paginate_by = 10


class AdvertisementDetail(DetailView):
    model = Advertisement
    template_name = 'advertisement_detail.html'
    context_object_name = 'advertisement'


