# Generated by Django 4.0.2 on 2022-03-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_rename_image_chatmodel_img_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmodel',
            name='message',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
