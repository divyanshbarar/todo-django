# Generated by Django 3.1 on 2020-09-07 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='creates',
            new_name='created',
        ),
    ]
