# Generated by Django 2.0.1 on 2018-01-15 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_car', '0002_auto_20180115_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='year',
            field=models.DateField(auto_now=True),
        ),
    ]
