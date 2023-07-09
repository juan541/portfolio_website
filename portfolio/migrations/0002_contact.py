# Generated by Django 4.2.3 on 2023-07-09 22:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('date_submittted', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
