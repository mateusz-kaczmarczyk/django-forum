# Generated by Django 3.1.4 on 2020-12-10 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subforum',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
