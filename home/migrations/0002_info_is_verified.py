# Generated by Django 3.1.7 on 2021-04-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]