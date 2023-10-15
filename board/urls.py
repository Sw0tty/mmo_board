from django.urls import path
from board.views import AdvertisementsList

urlpatterns = [
    path('', AdvertisementsList.as_view())
]
