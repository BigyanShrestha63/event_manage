# Generated by Django 5.1 on 2024-08-23 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EventManager', '0012_eventvenue_venueimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventvenue',
            name='google_maps_url',
            field=models.TextField(),
        ),
    ]
