from django.http import JsonResponse
from .models import Order

# заказ
def order_adding(request):
    return_dict = dict()
    data = request.POST
    car = data.get('car')
    name = data.get('name')
    phone = data.get('phone')
    srok = data.get('srok')
    Order.objects.create(car=car,
                         name=name,
                         phone=phone,
                         deadline=srok)
    return JsonResponse(return_dict)

