# Generated by Django 3.2.8 on 2021-12-03 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211203_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='is_min',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
