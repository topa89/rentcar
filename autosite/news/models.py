from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'Заголовок')
    text = HTMLField()
    image = models.FileField(upload_to='news_files', verbose_name='Картинка')

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return '/news/{}'.format(self.id)

    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
        ordering = ["-id"]    