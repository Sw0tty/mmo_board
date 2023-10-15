from django.urls import path
from board.views import AdvertisementsList, AdvertisementDetail

urlpatterns = [
    path('', AdvertisementsList.as_view()),
    path('<int:pk>/', AdvertisementDetail.as_view()),
]
