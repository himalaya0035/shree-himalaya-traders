# Generated by Django 3.0.8 on 2020-07-24 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_orderitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phoneno',
        ),
    ]