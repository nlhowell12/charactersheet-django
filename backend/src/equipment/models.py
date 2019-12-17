from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from characters.equipment_choices import (
    SPELL_FAILURE_CHANCES, BODY_SLOT_CHOICES
    )
from characters.bonuses import (BONUS_TYPES)


class Equipment(models.Model):
    class Meta:
        verbose_name_plural = 'Equipment'

    item_name = models.CharField(max_length=50)
    weight = models.IntegerField()
    description = models.TextField(max_length=1000)
    body_slot = models.CharField(
        max_length=10, choices=BODY_SLOT_CHOICES,
        blank=True, null=True
        )

    def __str__(self):
        return self.item_name


class Weapon(Equipment):
    damage_dice = models.CharField(max_length=5)
    two_handed = models.BooleanField(default=False)
    crit_range = models.CharField(max_length=10, default='20/x2')
    range_increment = models.IntegerField(validators=[MinValueValidator(0)])


class Armor(Equipment):
    class Meta:
        verbose_name_plural = 'Armor'

    armor_bonus = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(8)])
    bonus_type = models.CharField(
        choices=BONUS_TYPES, default='armor', max_length=10)
    armor_check_penalty = models.IntegerField(
        validators=[MinValueValidator(0)], default=0)
    movement_penalty = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        choices=[(0, 'None'), (5, '5 ft'), (10, '10 ft')],
        default=0)
    spell_failure_chance = models.IntegerField(
        choices=SPELL_FAILURE_CHANCES, default=0)
