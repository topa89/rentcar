from django.shortcuts import render,  get_object_or_404
from .models import Auto, AutoImage
from news.models import News

def index(request):
    context = {
        'cars_special': Auto.objects.filter(category=1),
        'cars_chip': Auto.objects.filter(category=2),
        'cars_premium': Auto.objects.filter(category=11),
        'news': News.objects.all()[:3]
    }
    return render(request, 'rent_car/index.html', context)

# получить информацию об авто
def car_info(request, pk):
    car_list = {
        'car': Auto.objects.get(pk=pk),
        'car_img': AutoImage.objects.filter(auto=Auto.objects.get(pk=pk).id),
        }
    return render(request, 'rent_car/information.html', car_list)

def contacts(request):
    return render(request, 'rent_car/contacts.html')
