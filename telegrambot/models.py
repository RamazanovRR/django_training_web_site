from django.db import models

# Create your models here.
class TelegramSetting(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='чат id')
    tg_text = models.TextField(verbose_name='Сообщение')

    # выводит имя в БД для объекта
    def __str__(self):
        return self.tg_chat

    # переименовываем название таблицы и объекта
    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'
