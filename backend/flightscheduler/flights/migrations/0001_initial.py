# Generated by Django 3.0.4 on 2020-03-24 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=200)),
                ('fligth_no', models.CharField(max_length=10)),
                ('trip_type', models.CharField(default='', max_length=50)),
                ('departure_airport', models.CharField(max_length=10)),
                ('arrival_airport', models.CharField(max_length=10)),
                ('departure_date', models.DateField()),
                ('return_date', models.DateField()),
            ],
        ),
    ]
