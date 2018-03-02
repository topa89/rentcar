from django.shortcuts import render,  get_object_or_404
from .models import Auto


# Create your views here.
def index(request):
    context = {
        "cars_special": Auto.objects.filter(category=1),
        "cars_chip": Auto.objects.filter(category=2),
        "cars_premium": Auto.objects.filter(category=11),
    }
    return render(request, 'rent_car/index.html', context)


def car_info(request, pk):
    return render(request, 'rent_car/information.html', {"car": Auto.objects.get(pk=pk)})
