# Generated by Django 4.1 on 2022-09-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='artist',
            field=models.CharField(default='Unknown', max_length=64),
        ),
        migrations.AddField(
            model_name='listing',
            name='size',
            field=models.CharField(default='Unknown', max_length=64),
        ),
    ]
