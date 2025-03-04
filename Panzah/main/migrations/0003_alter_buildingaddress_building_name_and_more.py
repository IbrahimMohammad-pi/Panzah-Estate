# Generated by Django 5.1.6 on 2025-03-03 13:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_buildingaddress_category_rename_owner_landlord_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingaddress',
            name='building_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='buildingaddress',
            name='building_number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='current_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.landlord'),
        ),
    ]
