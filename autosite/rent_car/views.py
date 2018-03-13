from django.shortcuts import render,  get_object_or_404
from .models import Auto, AutoImage, Category
from news.models import News
from subscribers.forms import SubscriberForm

def index(request):
    subscriber_form =  SubscriberForm()

    context = {
        'cars_special': Auto.objects.filter(category=1),
        'cars_chip': Auto.objects.filter(category=2),
        'cars_premium': Auto.objects.filter(category=3),
        'news': News.objects.all()[:3],
        'form': subscriber_form,
    }
    return render(request, 'rent_car/index.html', context)

# получить информацию об авто
def car_info(request, pk):
    context = {
        'car': Auto.objects.get(pk=pk),
        'car_img': AutoImage.objects.filter(auto=Auto.objects.get(pk=pk).id),
        }
    return render(request, 'rent_car/information.html', context)

def contacts(request):
    return render(request, 'rent_car/contacts.html')
