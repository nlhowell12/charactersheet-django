from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from django.contrib.auth.models import User
from characters.models import Character
from characters.api.serializers import CharacterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    @action(detail=False, methods=['post'])
    def login(self, request, pk=None):
        data = request.data
        user = User.objects.filter(username=data['username']).first()
        try:
            if user.check_password(data['password']):
                characters = Character.objects.filter(player=user)
                print(characters)
                return Response({
                    'status': True,
                    'characters': [
                        CharacterSerializer(
                            character).data for character in characters]
                })
            else:
                return Response({
                    'status': False,
                    'error': 'Password is not correct.'
                })
        except Exception:
            return Response({
                'status': False,
                'error': 'User does not exist.'
            })
