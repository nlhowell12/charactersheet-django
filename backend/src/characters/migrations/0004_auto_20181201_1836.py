# Generated by Django 2.1.3 on 2018-12-01 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_auto_20181201_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='character_name',
            new_name='character_Name',
        ),
    ]
