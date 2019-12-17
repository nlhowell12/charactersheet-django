from rest_framework import viewsets

from characters.models import (
    Character
    )
from .serializers import (
    CharacterSerializer
    )


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()
