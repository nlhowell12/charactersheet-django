from django.contrib import admin
from .models import (
    Equipment, Weapon,
    Armor
    )

admin.site.register(Equipment)
admin.site.register(Weapon)
admin.site.register(Armor)
