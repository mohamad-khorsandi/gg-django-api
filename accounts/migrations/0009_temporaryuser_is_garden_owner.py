# Generated by Django 4.2 on 2023-05-31 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_normaluser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporaryuser',
            name='is_garden_owner',
            field=models.BooleanField(default=False),
        ),
    ]