from django.contrib import admin
from .models import (
    Character, Race, Subrace,
    CharacterClass, Skill,
    Feat, Equipment, Weapon,
    Armor, BaseClass
    )

admin.site.register(Character)
admin.site.register(Race)
admin.site.register(Subrace)
admin.site.register(BaseClass)
admin.site.register(CharacterClass)
admin.site.register(Skill)
admin.site.register(Feat)
admin.site.register(Equipment)
admin.site.register(Weapon)
admin.site.register(Armor)
