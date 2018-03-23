from django.core.cache import cache
from celery.decorators import periodic_task
from celery.task.schedules import crontab

from news.models import News


@periodic_task(run_every=(crontab(minute='*/30')),
               name='last_news_caching',
               ignore_result=True,)
def last_news_caching():
    news = News.objects.all()[:3]
    i = 0
    for key in news:
        cache.set('tiding' + str(i), [key.title, key.text, key.image])
        i += 1