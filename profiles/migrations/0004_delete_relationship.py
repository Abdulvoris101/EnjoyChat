# Generated by Django 4.0.2 on 2022-02-26 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_remove_profile_friends_profile_follow'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RelationShip',
        ),
    ]
