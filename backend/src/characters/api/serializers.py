from rest_framework import serializers

from characters.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = (
            'id', 'character_Name', 'race', 'character_Classes',
            'hair_Color', 'eye_Color', 'height', 'weight', 'age',
            'max_HP', 'current_HP', 'base_Strength', 'base_Dexterity',
            'base_Constitution', 'base_Intelligence', 'base_Wisdom',
            'base_Charisma', 'personal_Traits', 'ideals',
            'flaws', 'notes', 'sex', 'alignment', 'zodiac_Sign',
            'skills', 'feats'
            )
