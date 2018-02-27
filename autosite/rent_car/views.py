from django.shortcuts import render
from .models import Auto


# Create your views here.
def index(request):
    context = {
        "cars_special": Auto.objects.filter(category=1),
        "cars_chip": Auto.objects.filter(category=2),
        "cars_premium": Auto.objects.filter(category=11),
    }
    return render(request, 'rent_car/index.html', context)


def info(request):
    return render(request, 'rent_car/information.html')
