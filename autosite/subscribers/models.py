from django.db import models


class Subscribers(models.Model):
    email = models.CharField(max_length=30)

    def __str__(self):
        return '%s' % (self.email)

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'