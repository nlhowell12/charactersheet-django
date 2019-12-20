from spells.models import (
    Song, Arcane, Prayer,
    Chant, Power, DisciplinePower,
    Vestige, MartialManeuver, Invocation,
    PactInvocation, Mystery
)
from characters.models import BaseClass
from xlrd import open_workbook


def spell_model(class_name):
    switcher = {
        'Bard': Song
    }
    return switcher[class_name]


def create_spell_model(class_name, data):
    associated_class = BaseClass.objects.filter(
        class_name=class_name).first()

    if class_name == 'Bard':
        spell_model(class_name).objects.create(
            chord=data[2].value,
            name=data[1].value,
            class_spell_list=associated_class,
            level=int(data[0].value),
            descriptors=data[3].value,
            casting_time=data[4].value,
            spell_range=data[5].value,
            duration=data[6].value,
            spell_save=data[7].value,
            bonus_type=data[8].value,
            damage_type=data[9].value,
            description=data[10].value
        )


def populate_spell_data(file_location):
    book = open_workbook(file_location)
    sheet = book.sheets()[0]
    rows = sheet.get_rows()
    for row in rows:
        if row[0].ctype == 2:
            create_spell_model(sheet.name, row)
