from rest_framework import serializers

from characters.models import (
    Character, Race, Subrace, BaseClass,
    Feat, CharacterClass
    )
from django.contrib.auth.models import User
from equipment.models import (
    Equipment
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = [
            'racial_name', 'attribute_bonuses', 'skill_bonuses',
            'description', 'special_abilities', 'playable'
            ]


class SubraceSerializer(serializers.ModelSerializer):
    race = RaceSerializer()

    class Meta:
        model = Subrace
        fields = [
            'race', 'subrace_name', 'attribute_bonuses',
            'skill_bonuses', 'description', 'special_abilities'
        ]


class BaseClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseClass
        fields = [
            'class_name', 'hit_die', 'class_skills', 'skill_points',
            'class_abilities', 'fort', 'reflex', 'will'
        ]


class CharacterClassSerializer(serializers.ModelSerializer):
    base_class = BaseClassSerializer()

    class Meta:
        model = CharacterClass
        fields = '__all__'


class FeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feat
        fields = [
            'feat_name', 'benefit', 'prerequisites',
            'skill_bonuses', 'attribute_bonuses'
        ]


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    character_classes = CharacterClassSerializer(many=True)
    feats = FeatSerializer(many=True)
    player = UserSerializer()
    DM = UserSerializer()
    race = RaceSerializer()
    subrace = SubraceSerializer()

    class Meta:
        model = Character
        fields = '__all__'
