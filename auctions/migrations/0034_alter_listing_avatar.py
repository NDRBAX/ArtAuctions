# Generated by Django 4.1 on 2022-09-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0033_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='avatar',
            field=models.URLField(blank=True, null=True),
        ),
    ]
