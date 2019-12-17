from rest_framework import viewsets
from xlrd import open_workbook
from rest_framework.decorators import action
from rest_framework.response import Response

from equipment.models import (
    Equipment
)
from .serializers import (
    EquipmentSerializer
    )


class EquipmentViewset(viewsets.ViewSet):
    serializer_class = EquipmentSerializer
    queryset = Equipment.objects.all()

    def list(self, request):
        return Response({'status': 'good'})

    @action(detail=False, methods=['post'])
    def populate_data(self, request, pk=None):
        # filename = request.FILES['filepath']
        worksheet = open_workbook(request.body)
        return Response(worksheet)
