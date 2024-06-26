# Generated by Django 2.2.6 on 2019-10-15 10:49

from django.db import migrations, models
import rota.models


class Migration(migrations.Migration):

    dependencies = [
        ('rota', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dateactive',
            options={'verbose_name': 'Active Date'},
        ),
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name': 'Member'},
        ),
        migrations.AlterField(
            model_name='dateactive',
            name='enddate',
            field=models.DateTimeField(default=rota.models.DateActive.default_end_time, max_length=250),
        ),
        migrations.AlterField(
            model_name='dateactive',
            name='startdate',
            field=models.DateTimeField(default=rota.models.DateActive.default_start_time, max_length=250),
        ),
        migrations.AlterField(
            model_name='members',
            name='mobile',
            field=models.CharField(max_length=11, verbose_name='Phone Number'),
        ),
    ]
