from django.contrib import admin
from .models import (
    Character, Race, Subrace,
    CharacterClass, Skill, CharacterSkill,
    Feat, Equipment, Weapon,
    Armor, SkillBonus, AttributeBonus
    )

admin.site.register(Character)
admin.site.register(Race)
admin.site.register(Subrace)
admin.site.register(CharacterClass)
admin.site.register(Skill)
admin.site.register(CharacterSkill)
admin.site.register(Feat)
admin.site.register(Equipment)
admin.site.register(Weapon)
admin.site.register(Armor)
admin.site.register(SkillBonus)
admin.site.register(AttributeBonus)
