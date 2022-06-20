# Generated by Django 4.0.2 on 2022-03-17 15:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(upload_to='posts/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'webp', 'jpeg', 'mp4', 'mkv'])]),
        ),
    ]