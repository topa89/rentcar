import math
from django.shortcuts import render

from .models import News
from random import sample
# пагинатор
def get_pages_amount():
    pages_content = {}
    news = News.objects.order_by('-id')
    count_news = News.objects.count()
    # число отображаемого контента задается здесь
    pages = math.ceil(count_news / 12)
    pages_count = 0

    for i in range(1, pages+1):
        pages_content[i] = news[pages_count:i * 12]
        pages_count += (i*12)

    return pages_content

# получить номер страницы новости
def get_page_number(num):
    page = get_pages_amount()
    return page[num]

# получить новости
def get_news(request):
    context = {
        'news': get_page_number(1),
        'pages': get_pages_amount(),
        }
    return render(request, 'news/index.html', context)

# получить номер страницы новости
def show_page_news(request, pk):
    context = {'news': get_page_number(int(pk)),
               'pages': get_pages_amount()}
    return render(request, 'news/index.html', context)

# показать новость и  еще рандомные новости
def show_news(request, pk):
    count = News.objects.all().count()
    rand_news = sample(range(1, count), 10)
    context = {'news': News.objects.get(pk=pk),
               'more_news': News.objects.filter(id__in=rand_news).exclude(pk=pk)}
    return render(request, 'news/news.html', context)

