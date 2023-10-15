from django.db import models
from django.contrib.auth.models import User

from board.resources import advertisement_type


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255, choices=advertisement_type)
    author_id = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='author')
    responses_id = models.ManyToManyField('ResponseModel', through='AdvertisementResponses')

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.user.username


class AdvertisementResponses(models.Model):
    advertisement_id = models.ForeignKey('Advertisement', on_delete=models.CASCADE)
    responses_id = models.ForeignKey('ResponseModel', on_delete=models.CASCADE)


class ResponseModel(models.Model):
    description = models.TextField()
    author_id = models.ForeignKey('Author', on_delete=models.CASCADE)
