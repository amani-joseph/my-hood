# Generated by Django 4.0.3 on 2022-04-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhood', '0002_rename_title_neighbourhood_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
