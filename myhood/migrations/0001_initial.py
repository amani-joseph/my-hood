# Generated by Django 4.0.3 on 2022-04-15 15:35

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile/')),
                ('bio', models.TextField(blank=True, default='My Bio', max_length=300, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=400)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('school', 'school'), ('gym', 'gym'), ('gas-station', 'gas-station'), ('recreational', 'recreational'), ('religious', 'religious'), ('business', 'business'), ('shop', 'shop'), ('shopping-center', 'shopping-center'), ('residential', 'residential')], default='', max_length=100)),
                ('Neighbourhood_location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='myhood.neighbourhood')),
            ],
        ),
    ]
