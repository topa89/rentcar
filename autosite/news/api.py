from tastypie.resources import ModelResource
from .models import News

class NewsResource(ModelResource):
    class Meta:
        queryset = News.objects.all()[:10]
        resource_name = 'tidings'