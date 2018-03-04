from django.shortcuts import render,  get_object_or_404
from .models import Auto
from django.http import JsonResponse
from .models import Order

def index(request):
    context = {
        "cars_special": Auto.objects.filter(category=1),
        "cars_chip": Auto.objects.filter(category=2),
        "cars_premium": Auto.objects.filter(category=11),
    }
    return render(request, 'rent_car/index.html', context)

# получить информацию об авто
def car_info(request, pk):
    return render(request, 'rent_car/information.html', {"car": Auto.objects.get(pk=pk)})

# заказ 
def order_adding(request):
    return_dict = dict()
    data = request.POST
    car = data.get('car')
    name = data.get('name')
    phone = data.get('phone')
    srok = data.get('srok')
    new_order = Order.objects.save(car=car, name=name, phone=phone, deadline=srok)
    return JsonResponse(return_dict)
