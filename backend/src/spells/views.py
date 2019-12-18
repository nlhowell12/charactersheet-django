from rest_framework import viewsets
from xlrd import open_workbook
from rest_framework.decorators import action
from rest_framework.response import Response
from spells.models import (
    Spell, Song, Arcane, Prayer,
    Chant, Power, DisciplinePower,
    Vestige, MartialManeuver, Invocation,
    PactInvocation, Mystery

)
from characters.models import BaseClass
from .serializers import (
    SpellSerializer
    )


def parse_sheet(sheet):
    parsed_sheet = dict()
    rows = sheet.get_rows()
    for row in rows:
        if(row[0].ctype == 2):
            parsed_sheet[row[1].value] = {
                'level': int(row[0].value),
                school_descriptor(sheet): row[2].value,
                'descriptors': row[3].value,
                'casting_time': row[4].value,
                'spell_range': row[5].value,
                'duration': row[6].value,
                'save': row[7].value,
                'bonus_type': row[8].value,
                'damage_type': row[9].value,
                'description': row[10].value
            }
    return parsed_sheet


def school_descriptor(sheet):
    switcher = {
        'Bard': 'chord',
        'Cleric': 'domain',
        'Druid': 'sphere',
        'Hexblade': 'school',
        'Oathsworn': 'domain/sphere',
        'Psion': 'discipline',
        'Psychic Warrior': 'discipline',
        'Sorcerer-Wizard': 'school'
    }
    return switcher[sheet.name]


def spell_model(sheet):
    switcher = {
        'Bard': Song,
        'Cleric': Prayer,
        'Druid':  Prayer,
        'Hexblade': Arcane,
        'Oathsworn': Prayer,
        'Psion': Power,
        'Psychic Warrior': Power,
        'Sorcerer-Wizard': Arcane
    }
    return switcher[sheet.name]


class SpellViewset(viewsets.ViewSet):
    serializer_class = SpellSerializer
    queryset = Spell.objects.all()

    def list(self, request):
        return Response({'status': 'good'})

    @action(detail=False, methods=['post'])
    def populate_data(self, request, pk=None):
        file_location = 'Spell-Lists.xls'
        book = open_workbook(file_location)
        sheets = book.sheets()
        spell_casting_classes = [
            'Bard', 'Cleric', 'Druid',
            'Hexblade', 'Oathsworn', 'Psion',
            'Psychic Warrior', 'Sorcerer-Wizard'
            ]
        for sheet in sheets:
            base_class = BaseClass.objects.filter(
                class_name=sheet.name).first()
            if sheet.name in spell_casting_classes:
                parsed_sheet = parse_sheet(sheet)
                for key, value in parsed_sheet.items():
                    print(key, value)
                    spell_model(sheet).objects.create(
                        name=key,
                        **value
                    )
        return Response()
