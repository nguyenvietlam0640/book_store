# Generated by Django 4.1.5 on 2023-03-12 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_user_creation_date'),
        ('products', '0017_alter_comment_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='authentication.user'),
        ),
    ]