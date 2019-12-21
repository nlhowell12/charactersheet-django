from django.contrib import admin
from .models import (
    Song, Prayer, Chant, Psion, PsychicWarrior,
    DisciplinePower, Vestige, Oathsworn,
    MartialManeuver, Invocation,
    PactInvocation, Mystery, Hexblade, Wizard
    )

admin.site.register(Song)
admin.site.register(Prayer)
admin.site.register(Chant)
admin.site.register(Psion)
admin.site.register(PsychicWarrior)
admin.site.register(DisciplinePower)
admin.site.register(Vestige)
admin.site.register(MartialManeuver)
admin.site.register(Invocation)
admin.site.register(PactInvocation)
admin.site.register(Mystery)
admin.site.register(Oathsworn)
admin.site.register(Hexblade)
admin.site.register(Wizard)
