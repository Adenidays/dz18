# Generated by Django 4.2.3 on 2023-07-06 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_alter_todolist_options_alter_todolist_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='priority',
            field=models.CharField(choices=[('Малый', 1), ('Высокий', 3), ('Средний', 2)], max_length=10),
        ),
    ]
