from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """При создании нового пользователя создает его токен аутентификации"""
    if created:
        Token.objects.create(user=instance)


class Task(models.Model):
    """Модель Задача.

    title -- название задачи, максимальная длинна 250 символов.
    content -- описание задачи (чтосделать), поле может быть пустым.
    created -- дата создания задачи, указывается в формате 'YYYY-MM-DD',
    если не указано другое, автоматически указывается текущая дата.
    """
    title: str = models.CharField(verbose_name="Название задачи", max_length=250)
    content: str = models.TextField(verbose_name="Описание задачи", blank=True)
    created: str = models.DateField(
        verbose_name="Дата создания задачи",
        default=timezone.now().strftime("%Y-%m-%d")
    )

    def __str__(self):
        return self.title
