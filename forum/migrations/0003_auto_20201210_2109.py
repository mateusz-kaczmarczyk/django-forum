# Generated by Django 3.1.4 on 2020-12-10 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20201210_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subforum',
            name='description',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
