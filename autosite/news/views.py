import math
from django.shortcuts import render,  get_object_or_404

from .models import News

def get_pages_amount():
    pages_content = {}
    news = News.objects.order_by('-id')
  
    count_news = News.objects.count()
    pages = math.ceil(count_news / 12) # число отображаемого контента задается здесь 
    pages_count = 0

    for i in range(1, pages+1):
        pages_content[i] = news[pages_count:i * 12]
        pages_count += (i*12)

    return pages_content


def get_page_number(num):
    page = get_pages_amount()
    return page[num]


def get_news(request):
    news = News.objects.all()
    page = get_pages_amount()

    context = {
        'news': get_page_number(1),
        'pages': get_pages_amount(),
        }
    return render(request, 'news/index.html', context)


def show_page_news(request, num):
    context = {'page': get_page_number(num),}
    return render(request, 'news/index.html', context)


def show_news(request, pk):
    context = {'news': News.objects.get(pk=pk)}
    return render(request, 'news/news.html', context )

