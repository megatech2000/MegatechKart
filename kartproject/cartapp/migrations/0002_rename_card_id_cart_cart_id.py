# Generated by Django 4.2.4 on 2023-11-29 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='card_id',
            new_name='cart_id',
        ),
    ]
