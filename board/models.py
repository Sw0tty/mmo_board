from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.mail import send_mail
from mmo_board.settings import DEFAULT_FROM_EMAIL

from board.resources import advertisement_type


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255, choices=advertisement_type)
    datetime_in = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='advertisement_images/', null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('advertisement_detail', args=[str(self.id)])


class Reply(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    adopted = models.BooleanField(default=False)
    advertisement_id = models.ForeignKey('Advertisement', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('reply_added')
    
    def send_notification_email(self):
        subject = "На ваше объявление поступил новый отклик"
        message = f'Здравствуйте!\n\nНа ваше объявление "{Advertisement.objects.get(id=self.advertisement_id).title[:15]}" появился новый отклик.'
        from_email = DEFAULT_FROM_EMAIL
        recipient_list = [Advertisement.objects.get(id=self.advertisement_id).author]
        return send_mail(subject, message, from_email, recipient_list)

    def send_accepted_email(self):
        subject = 'Ваш отклик принят'
        message = f'Здравствуйте!\n\nВаш отклик "{self.description[:15]}" принят.'
        from_email = DEFAULT_FROM_EMAIL
        recipient_list = [self.author.email]
        return send_mail(subject, message, from_email, recipient_list)
