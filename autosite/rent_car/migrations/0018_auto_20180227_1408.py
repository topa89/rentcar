# Generated by Django 2.0.2 on 2018-02-27 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_car', '0017_auto_mark'),
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
    ]