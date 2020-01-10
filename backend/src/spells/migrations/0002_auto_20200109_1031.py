# Generated by Django 3.0.2 on 2020-01-09 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spells', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chant',
            options={'ordering': ['level', 'name'], 'verbose_name_plural': 'Druid Chants'},
        ),
        migrations.AlterModelOptions(
            name='disciplinepower',
            options={'ordering': ['discipline_list', 'level', 'name'], 'verbose_name_plural': 'Discipline List Powers'},
        ),
        migrations.AlterModelOptions(
            name='hexblade',
            options={'ordering': ['level', 'name'], 'verbose_name_plural': 'Hexblade Spells'},
        ),
        migrations.AlterModelOptions(
            name='oathsworn',
            options={'ordering': ['level', 'name'], 'verbose_name_plural': 'Oathsworn Prayers'},
        ),
        migrations.AlterModelOptions(
            name='prayer',
            options={'ordering': ['level', 'name'], 'verbose_name_plural': 'Cleric Prayers'},
        ),
        migrations.AlterModelOptions(
            name='psion',
            options={'ordering': ['level', 'name'], 'verbose_name_plural': 'Psion Powers'},
        ),
        migrations.AlterModelOptions(
            name='psychicwarrior',
            options={'ordering': ['level', 'name'], 'verbose_name_plural': 'Psychic Warrior Powers'},
        ),
        migrations.AlterModelOptions(
            name='vestige',
            options={'ordering': ['name'], 'verbose_name_plural': 'Binder Vestiges'},
        ),
        migrations.AlterModelOptions(
            name='wizard',
            options={'ordering': ['level', 'name'], 'verbose_name_plural': 'Sorcerer - Wizard Spells'},
        ),
    ]