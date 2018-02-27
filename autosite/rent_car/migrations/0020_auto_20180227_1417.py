# Generated by Django 2.0.2 on 2018-02-27 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent_car', '0019_auto_20180227_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='mark',
        ),
        migrations.AddField(
            model_name='auto',
            name='mark',
            field=models.ManyToManyField(default=1, to='rent_car.MarkAuto', verbose_name='Марка авто'),
        ),
        migrations.RemoveField(
            model_name='auto',
            name='model',
        ),
        migrations.AddField(
            model_name='auto',
            name='model',
            field=models.ManyToManyField(default=0, to='rent_car.ModelAuto', verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='modelauto',
            name='mark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent_car.MarkAuto', verbose_name='Марка авто'),
        ),
    ]
