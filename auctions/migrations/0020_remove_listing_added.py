# Generated by Django 4.1 on 2022-09-09 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_listing_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='added',
        ),
    ]