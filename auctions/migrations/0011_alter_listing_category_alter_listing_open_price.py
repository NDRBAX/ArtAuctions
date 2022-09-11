# Generated by Django 4.1 on 2022-09-08 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_remove_listing_actual_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='listing',
            name='open_price',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10),
        ),
    ]