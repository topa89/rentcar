from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from rent_car import views
from orders.views import order_adding
from news.views import get_news, show_news, show_page_news
from subscribers.views import addSub

from news.api import NewsResource

news_resource = NewsResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^admin/tables/$', TemplateView.as_view(template_name='admin/tables.html')),
    path('', views.index, name='index'),
    path('car/<pk>', views.car_info, name='car_info'),
    # обработка заявок
    path('order_adding/', order_adding, name='order_adding'),
    path('add_sub', addSub, name='addSub'),
    # новости
    path('news/', get_news, name='get_news'),
    path('news/<pk>', show_news, name='show_news' ),
    path('news/page/<pk>', show_page_news, name='show_page_news'),

    path('category/<pk>', views.category, name='category'),

    path('developers', views.developers, name='developers'),
    path('contacts', views.contacts, name='contacts'),
    path('api/', include(news_resource.urls)),
    path('tinymce/', include('tinymce.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)