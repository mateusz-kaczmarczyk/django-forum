# Generated by Django 3.1.4 on 2021-02-04 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0011_auto_20210203_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='thread',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='forum.thread'),
            preserve_default=False,
        ),
    ]
