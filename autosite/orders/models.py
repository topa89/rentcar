from django.db import models

class Order(models.Model):
    car = models.CharField(max_length=100, verbose_name=u'Автомобиль')
    name = models.CharField(max_length=30, verbose_name=u'Имя')
    phone = models.CharField(max_length=20, verbose_name=u'Номер телефона')
    deadline = models.CharField(max_length=30, verbose_name=u'Срок аренды')
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}".format(self.car, self.phone)

    class Meta:
        verbose_name_plural = u'Заказы'