from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Task(models.Model):
    title = models.CharField(verbose_name="Название задачи", max_length=250)
    content = models.TextField(verbose_name="Описание задачи", blank=True)
    created = models.DateField(
        verbose_name="Дата создания задачи",
        default=timezone.now().strftime("%Y-%m-%d")
    )

    def __str__(self):
        return self.title
