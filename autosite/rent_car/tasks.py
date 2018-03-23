from celery.decorators import periodic_task
from celery.task.schedules import crontab

@periodic_task(
            run_every=(crontab(minute='*/30')),
            name='cars_caching',
            ignore_result=True,
        )
def cars_caching():
    print('1')
