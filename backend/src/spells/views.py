from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from spells.utils import populate_spell_data, get_spell_data


class SpellViewset(viewsets.ViewSet):

    def list(self, request):
        return Response({'status': 'good'})

    @action(detail=False, methods=['post'])
    def populate_spells(self, request, pk=None):
        try:
            spell_lists = request.FILES['SpellList']
            populate_spell_data(spell_lists)
            return Response({'Upload Successful'})
        except FileNotFoundError:
            return Response({
                'status': False,
                'error': 'File Not Found'
            })
        # except TypeError:
        #     return Response({
        #         'status': False,
        #         'error': 'Database write error'
        #     })
        except KeyError:
            return Response({
                'status': False,
                'error': 'KeyError, check dict'
            })

    @action(detail=False, methods=['get'])
    def get_spells(self, request, pk=None):
        get_spell_data()
        return Response({'got the spells'})
