# Generated by Django 4.0.3 on 2022-04-16 17:33

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('myhood', '0005_remove_category_neighbourhood_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='', max_length=63),
        ),
    ]
