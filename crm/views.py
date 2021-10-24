from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard
from price.models import PriceTable
from telegrambot.sendMessage import setTelegram

# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    pt_list = PriceTable.objects.all()
    form = OrderForm()
    obj_dictionary = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'pt_list': pt_list,
        'form': form
    }
    return render(request, './index.html', obj_dictionary)

def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    element = Order(order_name = name, order_phone = phone)
    element.save()
    setTelegram(tg_name = name, tg_phone = phone)
    return render(request, './thanks.html', {
        'name': name,
    })
