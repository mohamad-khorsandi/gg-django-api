# Generated by Django 4.2 on 2023-06-01 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_normaluser_allergy_compatible_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normaluser',
            name='allergy_compatible',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='attention_need',
            field=models.PositiveIntegerField(choices=[(1, 'Everyday'), (2, 'Weekly'), (3, 'Monthly')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='light_condition',
            field=models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='location_type_condition',
            field=models.PositiveIntegerField(choices=[(1, 'Apartment'), (2, 'Close'), (3, 'Open')], default=None, null=True),
        ),
        migrations.AlterField(
            model_name='normaluser',
            name='pet_compatible',
            field=models.BooleanField(default=None, null=True),
        ),
    ]
