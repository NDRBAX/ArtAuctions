# Generated by Django 4.1 on 2022-09-10 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0021_listing_is_it_in_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='is_it_in_watchlist',
        ),
    ]
