from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from xlrd import open_workbook

from characters.models import (
    Character, Feat
    )
from .serializers import (
    CharacterSerializer
    )


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()

    @action(detail=False, methods=['post'])
    def populate_feats(self, request, pk=None):
        try:
            file_location = 'Feat-List.xls'
            book = open_workbook(file_location)
            sheet = book.sheets()[0]
            rows = sheet.get_rows()
            for row in rows:
                Feat.objects.create(
                    feat_classification=row[0].value,
                    feat_name=row[1].value,
                    prerequisites=row[2].value,
                    benefit=row[3].value
                )
            return Response({'Upload successful'})
        except FileNotFoundError:
            return Response({
                'error': 'File Not Found',
                'status': False
            })
