from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from board.models import Advertisement
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from board.forms import CreatingAdvertisementForm


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


class AdvertisementCreate(LoginRequiredMixin, CreateView):
    model = Advertisement
    form_class = CreatingAdvertisementForm
    template_name = 'advertisement_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        return super().form_valid(form)


@login_required
def OwnAdvertisementsList(request):
    own_advertisements = Advertisement.objects.filter(author=request.user)
    context = {
        "own_advertisements": own_advertisements,
        }
    return render(request, "own_advertisements.html", context)
