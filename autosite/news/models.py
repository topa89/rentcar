from django.db import models
from django.core.mail import send_mail

from tinymce.models import HTMLField
from subscribers.models import Subscribers

class News(models.Model):
    title = models.CharField(max_length=50, verbose_name=u'Заголовок')
    text = HTMLField()
    image = models.FileField(upload_to='news_files', verbose_name='Картинка')

    def __str__(self):
        return "{}".format(self.title)

    def get_absolute_url(self):
        return '/news/{}'.format(self.id)

    def to_json(self):
        return {
            'title': self.title,
            'text': self.text,
            'url': self.get_absolute_url()
        }

    def save(self, *args, **kwargs):
        super(News, self).save(*args, **kwargs)
        lst = Subscribers.objects.all()
        sub_list = []
        for x in lst:
            sub_list.append(x.email)

        send_mail(
            'Аренда авто Новости',
            self.title + '\n' + self.text,
            'from@xsx.tim',
            sub_list,
            fail_silently=False,
        )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ["-id"]   