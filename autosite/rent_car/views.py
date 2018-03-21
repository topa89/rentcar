from django.shortcuts import render,  get_object_or_404
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.conf import settings

from .models import Auto, AutoImage, Category
from news.models import News
from subscribers.forms import SubscriberForm


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(CACHE_TTL)
def index(request):
    subscriber_form =  SubscriberForm()

    context = {
        'cars_special': Auto.objects.filter(category=1).order_by('-id'),
        'cars_chip': Auto.objects.filter(category=2).order_by('-id'),
        'cars_premium': Auto.objects.filter(category=3).order_by('-id'),
        'news': News.objects.order_by('-id')[:3],
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

def category(request, pk):
    context = {
        'cars': Auto.objects.filter(category = pk).order_by('-id')
    }
    return render(request, 'rent_car/cars_category.html', context)

def developers(request):
    return render(request, 'rent_car/developers.html')