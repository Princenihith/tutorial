# Generated by Django 2.0.4 on 2018-10-02 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20181002_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user_name',
            new_name='user',
        ),
    ]
