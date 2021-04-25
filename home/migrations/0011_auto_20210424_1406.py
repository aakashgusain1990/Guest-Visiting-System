# Generated by Django 3.1.7 on 2021-04-24 08:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_appointments'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='fname',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointments',
            name='vname',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
