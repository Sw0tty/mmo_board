from django.urls import path
from board.views import AdvertisementsList, AdvertisementDetail, OwnAdvertisementsList, AdvertisementCreate


urlpatterns = [
    path('', AdvertisementsList.as_view()),
    path('<int:pk>/', AdvertisementDetail.as_view(), name='advertisement_detail'),
    path('own/', OwnAdvertisementsList),
    path('create/', AdvertisementCreate.as_view()),
]
