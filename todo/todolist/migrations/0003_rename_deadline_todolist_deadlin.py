# Generated by Django 4.2.3 on 2023-07-06 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_alter_todolist_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='deadline',
            new_name='deadlin',
        ),
    ]
