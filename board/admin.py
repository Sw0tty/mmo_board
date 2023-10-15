from django.contrib import admin
from board.models import Advertisement, Author, AdvertisementResponses, ResponseModel

admin.site.register(Advertisement)
admin.site.register(Author)
admin.site.register(AdvertisementResponses)
admin.site.register(ResponseModel)
