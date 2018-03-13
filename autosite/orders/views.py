from django.shortcuts import render
from django.http import JsonResponse
from .models import Order
from rent_car.views import index

# заказ 
def order_adding(request):
    return_dict = dict()
    data = request.POST
    car = data.get('car')
    name = data.get('name')
    phone = data.get('phone')
    srok = data.get('srok')
    new_order = Order.objects.create(car=car, name=name, phone=phone, deadline=srok)
    return JsonResponse(return_dict)

