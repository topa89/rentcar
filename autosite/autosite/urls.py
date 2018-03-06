from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rent_car import views
from orders.views import order_adding
from news.views import get_news, show_news
from subscribers.views import sub_adding

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/tables/$', TemplateView.as_view(template_name='admin/tables.html')),
    url(r'^$', include('rent_car.urls')),
    url(r'^car/(?P<pk>\d+)/$', views.car_info, name='car_info'),

    url(r'order_adding/$', order_adding, name='order_adding'),
    url(r'^sub_adding/$', sub_adding, name='sub_adding'),

    url(r'news/$', get_news, name='get_news'),
    url(r'news/(?P<pk>\d+)/$', show_news, name='show_news' ),

    url(r'contacts/', views.contacts, name='contacts'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)