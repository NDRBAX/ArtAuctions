# Generated by Django 4.1 on 2022-09-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_remove_watchlist_listing_watchlist_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watchers', to='auctions.listing'),
        ),
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]
