from django.db import models

# verbose_name аргумент задает имя для поля внутри объекта в таблице
# Create your models here.
class Order(models.Model):
    order_dr = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Имя')
    order_phone = models.CharField(max_length=200, verbose_name='Телефон')

    # выводит имя в БД для объекта
    def __str__(self):
        return self.order_name

# переименовываем название таблицы и объекта
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'