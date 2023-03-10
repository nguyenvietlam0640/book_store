# Generated by Django 4.1.5 on 2023-02-26 05:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=1000)),
                ('phone', models.CharField(blank=True, max_length=12)),
                ('birthday', models.DateField(default=datetime.date(2023, 2, 26))),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2023, 2, 26, 12, 0, 21, 638930))),
            ],
            options={
                'ordering': ('email',),
            },
        ),
    ]
