# Generated by Django 2.1.2 on 2019-02-28 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_auto_20190301_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]