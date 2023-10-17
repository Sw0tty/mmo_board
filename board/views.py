from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from board.models import Advertisement, Reply
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from board.forms import CreatingAdvertisementForm, CreatingReplyForm, AdvertisementForm


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


class AdvertisementUpdate(LoginRequiredMixin, UpdateView):
    form_class = AdvertisementForm
    model = Advertisement
    
    template_name = 'advertisement_create.html'


class AdvertisementDelete(DeleteView):
    model = Advertisement
    template_name = 'advertisement_delete_page.html'
    success_url = reverse_lazy('advertisement_list')


def home_page(request):
    return render(request, "home.html")


@login_required
def own_advertisements_list(request):
    own_advertisements = Advertisement.objects.filter(author=request.user)
    context = {
            "own_advertisements": own_advertisements,
        }
    return render(request, "own_advertisements.html", context)


class ReplyCreate(LoginRequiredMixin, CreateView):
    model = Reply
    form_class = CreatingReplyForm
    template_name = 'advertisement_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        # self.object.advertisement_id = Advertisement.objects.get(id)
        return super().form_valid(form)
    