from django.shortcuts import render,  get_object_or_404
from .models import News

def get_news(request):
    news_list = {'news': News.objects.all()[:16]}
    return render(request, 'news/index.html', news_list)

def show_news(request, pk):
    news_list = {'news': News.objects.get(pk=pk)}
    return render(request, 'news/news.html', news_list )

