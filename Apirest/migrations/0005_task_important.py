# Generated by Django 3.2 on 2022-11-09 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Apirest', '0004_auto_20221109_1533'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='important',
            field=models.BooleanField(default=False),
        ),
    ]
