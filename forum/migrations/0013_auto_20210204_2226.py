# Generated by Django 3.1.4 on 2021-02-04 21:26

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0012_auto_20210204_1709'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Comment',
        ),
    ]
