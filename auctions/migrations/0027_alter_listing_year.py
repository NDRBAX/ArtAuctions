# Generated by Django 4.1 on 2022-09-12 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0026_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='year',
            field=models.DateField(),
        ),
    ]
