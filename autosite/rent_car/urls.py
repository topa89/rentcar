from django.conf.urls import url

from . import views

app_name = 'project'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^info', views.info, name='info'),
]
