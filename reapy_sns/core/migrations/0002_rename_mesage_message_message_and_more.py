# Generated by Django 4.2.4 on 2023-08-15 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='mesage',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='nickName',
            new_name='nickname',
        ),
    ]
