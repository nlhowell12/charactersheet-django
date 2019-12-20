from django.contrib import admin
from .models import (
    Song, Prayer, Chant, Power,
    DisciplinePower, Vestige,
    MartialManeuver, Invocation,
    PactInvocation, Mystery
    )

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
