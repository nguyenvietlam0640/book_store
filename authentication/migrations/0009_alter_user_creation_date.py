# Generated by Django 4.1.5 on 2023-03-17 04:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_user_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 17, 11, 2, 38, 666136)),
        ),
    ]