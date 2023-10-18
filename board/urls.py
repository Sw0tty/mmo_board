from django.urls import path
from board import views


urlpatterns = [
    path('', views.AdvertisementsList.as_view(), name='advertisement_list'),
    path('<int:pk>/', views.AdvertisementDetail.as_view(), name='advertisement_detail'),
    path('own/', views.own_advertisements_list),
    path('create/', views.AdvertisementCreate.as_view()),
    path('<int:pk>/edit/delete/', views.AdvertisementDelete.as_view(), name='advertisement_delete'),
    path('<int:pk>/reply/', views.ReplyCreate.as_view(), name='reply_create'),
    path('<int:pk>/reply/added/', views.reply_added_page, name='reply_added'),
    path('<int:pk>/edit/', views.AdvertisementUpdate.as_view(), name='advertisement_edit'),
]
