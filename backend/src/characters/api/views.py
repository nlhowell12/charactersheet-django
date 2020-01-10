from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .utils import (
    generate_feats, serve_feats, add_new_character
    )
from characters.models import (
    Character, BaseClass
    )
from .serializers import (
    CharacterSerializer
    )


def serve_classes(data):
    classes = {}
    for base_class in data:
        classes[base_class.class_name] = {
            'hit_die': base_class.hit_die,
            'base_attack_bonus': base_class.base_attack_bonus,
            'skill_points': base_class.skill_points,
            'class_abilities': base_class.class_abilities,
            'fort': base_class.fort,
            'reflex': base_class.reflex,
            'will': base_class.will,
            'spells_per_level': base_class.spells_per_level,
            'spells_known': base_class.spells_known
        }
    return classes


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

    @action(detail=False, methods=['get', 'post'])
    def classes(self, request, pk=None):
        all_classes = BaseClass.objects.all()
        return Response(serve_classes(all_classes))

    @action(detail=False, methods=['get'])
    def get_feats(self, request, pk=None):
        return Response(serve_feats())

    @action(detail=False, methods=['put'])
    def add_character(self, request, pk=None):
        character = request.data
        response = add_new_character(character)
        return Response(response)

    @action(detail=False, methods=['get'])
    def get_character(self, request, pk=None):
        character_name = request.GET.get(key='name')
        character = Character.objects.get(character_name=character_name)
        return Response(CharacterSerializer(character).data)
