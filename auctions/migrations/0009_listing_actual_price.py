# Generated by Django 4.1 on 2022-09-07 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_listing_open_price_alter_listing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='actual_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]