from rest_framework import serializers

from characters.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('id', 'character_Name', 'hair_Color', 'eye_Color', 'height', 'age', 'max_HP', 'base_Strength', 'base_Dexterity', 'base_Constitution', 'base_Intelligence', 'base_Wisdom', 'base_Charisma', 'personal_Traits', 'ideals', 'flaws', 'notes')
