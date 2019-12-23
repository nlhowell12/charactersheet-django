from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .utils import generate_feats
from characters.models import (
    Character
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
            feat_lists = request.FILES['FeatList']
            generate_feats(feat_lists)
            return Response({'Upload successful'})
        except FileNotFoundError:
            return Response({
                'error': 'File Not Found',
                'status': False
            })
