# coding=utf-8
from django.db import models


class Category(models.Model):
    name = models.CharField(u'Название', max_length=20)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = u'Категории авто'

    # Create your models here.


class MarkAuto(models.Model):
    title = models.CharField(
        u'Марка',
        max_length=20
    )

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        verbose_name_plural = u'Марки авто'


class ModelAuto(models.Model):
    mark = models.ForeignKey(
        MarkAuto,
        on_delete=models.CASCADE,
        verbose_name=u'Марка авто'
    )
    name = models.CharField(max_length=25)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = u'Модели авто'


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

    model = models.OneToOneField(
        ModelAuto,
        verbose_name=u'Модель',
        on_delete=models.CASCADE,
        default=0
    )
    year = models.CharField(
        u'Год выпуска',
        max_length=4,
        default=u'2018'
    )

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
        return "{} {}".format(self.mark, self.model)

    class Meta:
        verbose_name_plural = u'Авто'


