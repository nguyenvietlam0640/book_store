# Generated by Django 4.1.5 on 2023-03-10 17:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 0, 57, 32, 337707)),
        ),
    ]
