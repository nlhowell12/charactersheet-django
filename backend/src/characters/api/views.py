from rest_framework import viewsets

from characters.models import Character
from .serializers import CharacterSerializer


class CharacterViewSet(viewsets.ModelViewSet):
    serializer_class = CharacterSerializer
    queryset = Character.objects.all()


# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     DestroyAPIView,
#     UpdateAPIView
# )

# class CharacterListView(ListAPIView):
#     queryset = Character.objects.all()
#     serializer_class = CharacterSerializer


# class CharacterDetailView(RetrieveAPIView):
#     queryset = Character.objects.all()
#     serializer_class = CharacterSerializer


# class CharacterCreateView(CreateAPIView):
#     queryset = Character.objects.all()
#     serializer_class = CharacterSerializer


# class CharacterUpdateView(UpdateAPIView):
#     queryset = Character.objects.all()
#     serializer_class = CharacterSerializer


# class CharacterDeleteView(DestroyAPIView):
#     queryset = Character.objects.all()
#     serializer_class = CharacterSerializer