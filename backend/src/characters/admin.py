from django.contrib import admin
from .models import (
    Character, Race, Subrace,
    CharacterClass, Skill,
    Feat, Equipment, Weapon,
    Armor, BaseClass, Spell,
    Song, Prayer, Chant, Power,
    DisciplinePower, Vestige,
    MartialManeuver, Invocation,
    PactInvocation, Mystery
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
admin.site.register(Spell)
admin.site.register(Song)
admin.site.register(Prayer)
admin.site.register(Chant)
admin.site.register(Power)
admin.site.register(DisciplinePower)
admin.site.register(Vestige)
admin.site.register(MartialManeuver)
admin.site.register(Invocation)
admin.site.register(PactInvocation)
admin.site.register(Mystery)
