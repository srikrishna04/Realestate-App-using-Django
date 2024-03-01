# Generated by Django 4.1.7 on 2023-03-05 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('num_bedrooms', models.IntegerField()),
                ('num_halls', models.IntegerField()),
                ('Square_footage', models.IntegerField()),
            ],
        ),
    ]