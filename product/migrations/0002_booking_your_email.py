# Generated by Django 4.0 on 2022-02-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='your_email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
