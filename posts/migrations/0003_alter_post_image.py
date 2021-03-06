# Generated by Django 4.0.2 on 2022-02-23 17:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='posts/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'webp', 'jpeg'])]),
        ),
    ]
