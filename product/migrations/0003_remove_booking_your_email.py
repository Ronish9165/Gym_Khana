# Generated by Django 4.0 on 2022-02-20 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_booking_your_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='your_email',
        ),
    ]