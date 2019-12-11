from rest_framework import serializers

from characters.models import (
    Character, Race, Subrace, BaseClass,
    Skill, Feat, Equipment
    )


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [
            'id', 'player', 'DM', 'character_Name', 'race',
            'character_Classes', 'hair_Color', 'eye_Color',
            'height', 'weight', 'age',
            'max_HP', 'current_HP', 'base_Strength', 'base_Dexterity',
            'base_Constitution', 'base_Intelligence', 'base_Wisdom',
            'base_Charisma', 'personal_Traits', 'ideals',
            'flaws', 'notes', 'sex', 'alignment', 'zodiac_Sign',
            'skills', 'feats'
            ]


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = [
            'racial_name', 'attribute_bonuses', 'skill_bonuses',
            'description', 'special_abilities', 'non_playable'
            ]


class SubraceSerializer(serializers.ModelSerializer):
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
            'hit_die', 'class_skills', 'skill_points',
            'class_abilities', 'fort', 'reflex', 'will'
        ]


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = [
            'skill_name', 'synergies', 'description',
        ]


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
