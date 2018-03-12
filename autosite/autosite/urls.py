from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rent_car import views
from orders.views import order_adding
from news.views import get_news, show_news
from subscribers.views import sub_adding

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^admin/tables/$', TemplateView.as_view(template_name='admin/tables.html')),
    path('', include('rent_car.urls')),
    path('car/<pk>', views.car_info, name='car_info'),

    path('order_adding/', order_adding, name='order_adding'),
    path('sub_adding/', sub_adding, name='sub_adding'),

    path('news/', get_news, name='get_news'),
    path('news/<pk>', show_news, name='show_news' ),

    path('contacts/', views.contacts, name='contacts'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)