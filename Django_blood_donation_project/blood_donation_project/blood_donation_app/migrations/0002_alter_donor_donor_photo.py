# Generated by Django 5.0.1 on 2024-02-21 10:29

import blood_donation_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donation_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='donor_photo',
            field=models.ImageField(blank=True, null=True, storage=blood_donation_app.models.S3MediaStorage(), upload_to='media'),
        ),
    ]