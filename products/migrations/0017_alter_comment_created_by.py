# Generated by Django 4.1.5 on 2023-03-12 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_user_creation_date'),
        ('products', '0016_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='authentication.user'),
        ),
    ]