# Generated by Django 3.0.2 on 2020-01-05 17:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20200105_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseclass',
            name='spells_known',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]