# Generated by Django 2.2.7 on 2019-12-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=13, verbose_name='Phone Number')),
            ],
        ),
    ]
