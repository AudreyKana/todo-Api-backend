# Generated by Django 3.2 on 2022-11-09 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Apirest', '0002_auto_20221109_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='periode',
        ),
    ]
