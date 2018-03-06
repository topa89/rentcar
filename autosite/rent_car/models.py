
from django.db import models


class Category(models.Model):
    name = models.CharField(u'Название', max_length=20)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = u'Категории авто'




class MarkAuto(models.Model):
    title = models.CharField(
        u'Марка',
        max_length=100
    )

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = u'Марки авто'



class Auto(models.Model):
    GEARS = tuple(enumerate(
        (u'Автомат',
         u'Механическая',
         )
    )
    )
    mark = models.OneToOneField(
        MarkAuto,
        default=1,
        on_delete=models.CASCADE,
        verbose_name=u'Марка авто'
    )
    category = models.ManyToManyField(
        Category,
        default=0,
        verbose_name=u'Категория'
    )

    year = models.CharField(
        u'Год выпуска',
        max_length=4,
        default=u'2018'
    )

    description = models.TextField(null=True, verbose_name='Описание')

    image = models.FileField(
        u'Изображение',
        blank=True,
        upload_to=u'auto'
    )
    gears = models.PositiveIntegerField(
        u'Коробка',
        choices=GEARS,
        default=0
    )
    engine = models.DecimalField(
        u'Двигатель',
        max_digits=2,
        decimal_places=1,
        default=1.6
    )
    min_age = models.PositiveIntegerField(
        u'Минимальный возраст',
        default=18
    )
    experience = models.PositiveIntegerField(
        u'Опыт вождения',
        default=3
    )
    price = models.PositiveIntegerField(
        u'Цена', default=1300
    )

    def __str__(self):
        return "{}".format(self.mark)

    class Meta:
        verbose_name_plural = u'Авто'

class AutoImage(models.Model):
    auto = models.ForeignKey(Auto, blank=True, null=True, default=None, on_delete=models.CASCADE )
    image = models.ImageField(upload_to='auto')

    def __str__(self):
        return "%s" % self.auto
    
    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'



