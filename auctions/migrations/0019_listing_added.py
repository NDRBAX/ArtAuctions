# Generated by Django 4.1 on 2022-09-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_user_watchlist_delete_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='added',
            field=models.BooleanField(default=False),
        ),
    ]