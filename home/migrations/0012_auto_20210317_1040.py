# Generated by Django 3.1.7 on 2021-03-17 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210317_0530'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='sNo',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 17, 10, 40, 30, 193236)),
        ),
    ]
