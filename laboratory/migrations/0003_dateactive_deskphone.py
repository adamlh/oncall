# Generated by Django 2.2.7 on 2019-12-10 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0002_sitelocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='dateactive',
            name='deskphone',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='laboratory.SiteLocation'),
            preserve_default=False,
        ),
    ]
