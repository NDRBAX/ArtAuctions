# Generated by Django 4.1 on 2022-09-13 08:12

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0031_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Antiques', 'Antiques'), ('Drawing', 'Drawing'), ('Watercolor', 'Watercolor'), ('Design', 'Design'), ('Miniature', 'Miniature'), ('Painting', 'Painting'), ('Photography', 'Photography'), ('Sculpture', 'Sculpture'), ('Prints', 'Prints'), ('Oil', 'Oil'), ('Acrylic', 'Acrylic'), ('Original artwork', 'Original artwork')], max_length=250),
        ),
    ]
