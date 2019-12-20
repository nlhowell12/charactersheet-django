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
from .serializers import (
    SpellSerializer
    )
from spells.utils import populate_spell_data


class SpellViewset(viewsets.ViewSet):

    def list(self, request):
        return Response({'status': 'good'})

    @action(detail=False, methods=['post'])
    def populate_spells(self, request, pk=None):
        try:
            populate_spell_data('Spell-Lists.xls')
            return Response({'Upload Successful'})
        except FileNotFoundError:
            return Response({
                'status': False,
                'error': 'File Not Found'
            })
