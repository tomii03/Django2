# Generated by Django 2.2 on 2020-08-06 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0003_auto_20200806_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='idd',
        ),
    ]