# Generated by Django 2.0.7 on 2018-12-02 02:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_auto_20181201_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='eye_Color',
            field=models.CharField(default='enter eye color', max_length=16),
        ),
        migrations.AddField(
            model_name='character',
            name='hair_Color',
            field=models.CharField(default='enter hair color', max_length=16),
        ),
        migrations.AddField(
            model_name='character',
            name='height',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='character',
            name='height_Units',
            field=models.CharField(default='enter height units', max_length=12),
        ),
        migrations.AlterField(
            model_name='character',
            name='character_Name',
            field=models.CharField(max_length=50),
        ),
    ]
