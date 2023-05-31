# Generated by Django 4.2 on 2023-05-31 14:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_temporaryuser_is_garden_owner'),
        ('garden', '0009_alter_garden_address_alter_garden_business_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='avg_score',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='garden',
            name='garden_owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.gardenownerprofile'),
        ),
    ]