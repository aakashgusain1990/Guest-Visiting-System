# Generated by Django 3.1.4 on 2021-04-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0006_details_db'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments_db',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('fullname_of_visitor', models.CharField(max_length=30)),
                ('purpose', models.CharField(max_length=50)),
                ('date_ofapp', models.DateField()),
            ],
        ),
    ]
