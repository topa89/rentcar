# Generated by Django 2.0.2 on 2018-02-27 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rent_car', '0016_auto_20180227_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='mark',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='rent_car.MarkAuto', verbose_name='Марка авто'),
        ),
    ]
