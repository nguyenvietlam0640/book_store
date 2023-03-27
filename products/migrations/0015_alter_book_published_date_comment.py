# Generated by Django 4.1.5 on 2023-03-10 13:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_user_creation_date'),
        ('products', '0014_alter_book_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='authentication.user')),
                ('created_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.book')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]