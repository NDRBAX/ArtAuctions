# Generated by Django 4.1 on 2022-09-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_alter_listing_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
