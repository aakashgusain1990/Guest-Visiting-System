# Generated by Django 3.1.4 on 2021-04-13 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_auto_20210413_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_db',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('uname', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
