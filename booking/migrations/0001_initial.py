# Generated by Django 2.1.7 on 2019-05-18 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('number_of_people', models.IntegerField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
