from spells.models import (
    Song, Wizard, Hexblade, Prayer,
    Chant, Psion, PsychicWarrior, DisciplinePower,
    Vestige, MartialManeuver, Invocation,
    PactInvocation, Mystery, Oathsworn
)
from characters.models import BaseClass
from xlrd import open_workbook


def spell_model(class_name):
    switcher = {
        'Bard': Song,
        'Cleric': Prayer,
        'Druid': Chant,
        'Hexblade': Hexblade,
        'Oathsworn': Oathsworn,
        'Psion': Psion,
        'Sorcerer - Wizard': Wizard,
        'Psychic Warrior': PsychicWarrior
    }
    return switcher[class_name]


def spell_descriptor(class_name):
    switcher = {
        'Bard': 'chord',
        'Cleric': 'domain',
        'Druid': 'sphere',
        'Hexblade': 'school',
        'Oathsworn': 'domain',
        'Psion': 'discipline',
        'Psychic Warrior': 'discipline',
        'Sorcerer - Wizard': 'school'
    }
    return switcher[class_name]


def create_spell_model(class_name, data):
    associated_class = BaseClass.objects.filter(
        class_name=class_name).first()
    values = {
        spell_descriptor(class_name): data[2].value,
        'name': data[1].value,
        'class_spell_list': associated_class,
        'level': int(data[0].value),
        'descriptors': data[3].value,
        'casting_time': data[4].value,
        'spell_range': data[5].value,
        'duration': data[6].value,
        'spell_save': data[7].value,
        'bonus_type': data[8].value,
        'damage_type': data[9].value,
        'description': data[10].value
    }
    spell_model(class_name).objects.create(
        **values
        )


def clear_spell_data():
    Song.objects.all().delete()
    Wizard.objects.all().delete()
    Hexblade.objects.all().delete()
    Prayer.objects.all().delete()
    Chant.objects.all().delete()
    Psion.objects.all().delete()
    PsychicWarrior.objects.all().delete()
    DisciplinePower.objects.all().delete()
    Vestige.objects.all().delete()
    MartialManeuver.objects.all().delete()
    Invocation.objects.all().delete()
    PactInvocation.objects.all().delete()
    Mystery.objects.all().delete()
    Oathsworn.objects.all().delete()


def populate_spell_data(file):
    clear_spell_data()
    book = open_workbook(file_contents=file.read())
    sheets = book.sheets()
    spell_casting_classes = [
        'Bard', 'Cleric', 'Druid', 'Hexblade',
        'Oathsworn', 'Psion',
        'Psychic Warrior', 'Sorcerer - Wizard'
    ]
    for sheet in sheets:
        print(sheet.name, ' - Started')
        rows = sheet.get_rows()
        for row in rows:
            if sheet.name in spell_casting_classes:
                if row[0].ctype == 2:
                    create_spell_model(sheet.name, row)
            elif sheet.name == 'Fighter':
                if row[0].ctype == 1:
                    MartialManeuver.objects.create(
                        name=row[2].value,
                        style=row[0].value,
                        level=row[1].value,
                        maneuver_type=row[3].value,
                        description=row[4].value
                    )
            elif sheet.name == 'Discipline Powers':
                if row[0].ctype == 1:
                    DisciplinePower.objects.create(
                        discipline_list=row[0].value,
                        name=row[1].value,
                        level=row[2].value,
                        descriptors=row[3].value,
                        casting_time=row[4].value,
                        spell_range=row[5].value,
                        duration=row[6].value,
                        spell_save=row[7].value,
                        bonus_type=row[8].value,
                        damage_type=row[9].value,
                        description=row[10].value
                    )
            elif sheet.name == 'Binder':
                if row[0].ctype == 2:
                    Vestige.objects.create(
                        name=row[1].value,
                        ruling_star=row[2].value,
                        summoning_req=row[3].value,
                        binding_DC=row[4].value,
                        strength=row[5].value,
                        tenacity=row[6].value,
                        force=row[7].value,
                        intellect=row[8].value,
                        will=row[9].value,
                        cunning=row[10].value
                    )
            elif sheet.name == 'Shadowcaster':
                if row[0].ctype == 1:
                    Mystery.objects.create(
                        name=row[1].value,
                        mystery_rank=row[0].value,
                        path=row[2].value,
                        mystery_range=row[3].value,
                        duration=row[4].value,
                        mystery_save=row[5].value,
                        description=row[6].value
                    )
            elif sheet.name == 'Warlock':
                if row[0].ctype == 1:
                    Invocation.objects.create(
                        grade=row[0].value,
                        name=row[1].value,
                        level_equivalent=row[2].value,
                        invocation_type=row[3].value,
                        duration=row[4].value,
                        invocation_save=row[5].value,
                        description=row[6].value
                    )
            elif sheet.name == 'Pact Invocations':
                if row[0].ctype == 1:
                    PactInvocation.objects.create(
                        grade=row[0].value,
                        pact=row[1].value,
                        name=row[2].value,
                        level_equivalent=row[3].value,
                        invocation_type=row[4].value,
                        duration=row[5].value,
                        invocation_save=row[6].value,
                        description=row[7].value,
                    )
        print(sheet.name, "- Complete")


def parse_spell(spell, class_name):
    return {
            'name': spell.name,
            'level': spell.level,
            'descriptors': spell.descriptors,
            'casting_time': spell.casting_time,
            'spell_range': spell.spell_range,
            'duration': spell.duration,
            'spell_save': spell.spell_save,
            'bonus_type': spell.bonus_type,
            'damage_type': spell.damage_type,
            'description': spell.description
        }


def get_spell_data():
    data = [
        ('Bard', Song.objects.all()),
        ('Wizard', Wizard.objects.all()),
        ('Hexblade', Hexblade.objects.all()),
        ('Cleric', Prayer.objects.all()),
        ('Druid', Chant.objects.all()),
        ('Psion', Psion.objects.all()),
        ('Psychic Warrior', PsychicWarrior.objects.all()),
        # ('discipline', DisciplinePower.objects.all()),
        # ('vestiges', Vestige.objects.all()),
        # ('martial_maneuvers', MartialManeuver.objects.all()),
        # ('invocations', Invocation.objects.all()),
        # ('pact_invocations', PactInvocation.objects.all()),
        # ('mysteries', Mystery.objects.all()),
        ('Oathsworn', Oathsworn.objects.all())
    ]
    parsed_spells = {
        spell_list[0]: [
            parse_spell(spell, spell_list[0]) for spell in spell_list[1]
            ]
        for spell_list in data
    }
    return parsed_spells
