# Generated by Django 3.1.7 on 2021-04-11 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_info_auth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='auth',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
