# Generated by Django 4.1.7 on 2023-03-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='Address',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
    ]
