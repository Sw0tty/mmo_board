from django.urls import path
from board.views import AdvertisementsList, AdvertisementDetail, own_advertisements_list, AdvertisementCreate, AdvertisementDelete, ReplyCreate, AdvertisementUpdate


urlpatterns = [
    path('', AdvertisementsList.as_view(), name='advertisement_list'),
    path('<int:pk>/', AdvertisementDetail.as_view(), name='advertisement_detail'),
    path('own/', own_advertisements_list),
    path('create/', AdvertisementCreate.as_view()),
    path('<int:pk>/edit/delete/', AdvertisementDelete.as_view(), name='advertisement_delete'),
    path('<int:pk>/reply/', ReplyCreate.as_view(), name='reply_create'),
    path('<int:pk>/edit/', AdvertisementUpdate.as_view(), name='advertisement_edit'),
]
