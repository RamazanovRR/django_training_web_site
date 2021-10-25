from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

class CommentOrd(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    # колличество отображаемых объектов
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    # отображает поля в таблице Заказов
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dr')
    # делает переданные поля кликабельными в таблице заказов, для открытия карточки
    list_display_links = ('id', 'order_name')
    # отображение поискового поля и поиска по нему производится по полям которые указаны в search_fields
    search_fields = ('id', 'order_name', 'order_phone', 'order_dr')
    # выводит фильтр по указанному полю (в данном решение работает со связкой)
    list_filter = ('order_status',)
    # задаются поля для редактирования
    list_editable = ('order_status', 'order_phone')
    # колличество элементов на страницу
    list_per_page = 5
    # колличество элементов при нажатии на кнопку "Показать все"
    list_max_show_all = 20
    inlines = [CommentOrd,]

    # Отображение полей в самой карточке Заказа
    fields = ('id', 'order_status',  'order_dr', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dr')

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
