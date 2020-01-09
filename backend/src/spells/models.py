from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from characters.models import BaseClass


class Spell(models.Model):
    class Meta:
        ordering = ['level', 'name']
        abstract = True

    name = models.CharField(max_length=50)
    level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        default=0)
    class_spell_list = models.ForeignKey(
        BaseClass, on_delete=models.CASCADE, null=True)
    descriptors = models.CharField(max_length=50, blank=True, null=True)
    casting_time = models.CharField(max_length=50, default="Standard Action")
    spell_range = models.CharField(max_length=50, default='Short')
    area = models.CharField(max_length=50, null=True, blank=True)
    duration = models.CharField(max_length=50, default='Instantaneous')
    spell_save = models.CharField(max_length=50, null=True, blank=True)
    bonus_type = models.CharField(max_length=50, null=True, blank=True)
    damage_type = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    spell_resistance = models.BooleanField(default=True)
    components = models.CharField(max_length=20, default='V, S, M')

    def __str__(self):
        return f'{self.level} - {self.name}'


class Song(Spell):
    class Meta:
        ordering = ['level', 'name']
    chord = models.CharField(max_length=20)


class Wizard(Spell):
    class Meta:
        verbose_name_plural = 'Sorcerer - Wizard Spells'
        ordering = ['level', 'name']

    school = models.CharField(max_length=20)


class Hexblade(Spell):
    class Meta:
        verbose_name_plural = 'Hexblade Spells'
        ordering = ['level', 'name']

    school = models.CharField(max_length=20)


class Prayer(Spell):
    class Meta:
        verbose_name_plural = 'Cleric Prayers'
        ordering = ['level', 'name']
    domain = models.CharField(max_length=20)


class Chant(Spell):
    class Meta:
        verbose_name_plural = 'Druid Chants'
        ordering = ['level', 'name']
    sphere = models.CharField(max_length=20)


class Oathsworn(Spell):
    class Meta:
        verbose_name_plural = 'Oathsworn Prayers'
        ordering = ['level', 'name']
    domain = models.CharField(max_length=20)


class Psion(Spell):
    class Meta:
        verbose_name_plural = 'Psion Powers'
        ordering = ['level', 'name']
    discipline = models.CharField(max_length=20)


class PsychicWarrior(Spell):
    class Meta:
        verbose_name_plural = 'Psychic Warrior Powers'
        ordering = ['level', 'name']
    discipline = models.CharField(max_length=20)


class DisciplinePower(Psion):
    class Meta:
        verbose_name_plural = 'Discipline List Powers'
        ordering = ['discipline_list', 'level', 'name']
    discipline_list = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.discipline_list} - {self.level} - {self.name}'


class Vestige(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Binder Vestiges'

    name = models.CharField(max_length=50)
    ruling_star = models.CharField(max_length=50)
    summoning_req = models.CharField(max_length=3)
    binding_DC = models.IntegerField(validators=[MinValueValidator(1)])
    strength = models.CharField(max_length=50)
    tenacity = models.CharField(max_length=50)
    force = models.CharField(max_length=50)
    intellect = models.CharField(max_length=50)
    will = models.CharField(max_length=50)
    cunning = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MartialManeuver(models.Model):
    class Meta:
        ordering = ['style', 'level', 'name']

    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    level = models.IntegerField(validators=[MinValueValidator(1)])
    maneuver_type = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.style} - {self.level} - {self.name}'


class Invocation(models.Model):
    class Meta:
        ordering = ['grade', 'level_equivalent', 'name']

    grade = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    level_equivalent = models.CharField(max_length=100, null=True, blank=True)
    invocation_type = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)
    invocation_save = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.grade} - {self.name}'


class PactInvocation(Invocation):
    pact = models.CharField(max_length=100)


class Mystery(models.Model):
    class Meta:
        verbose_name_plural = 'Mysteries'
        ordering = ['mystery_rank', 'path']

    name = models.CharField(max_length=50)
    mystery_rank = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    mystery_range = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    mystery_save = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.mystery_rank} - {self.path}. {self.name}'


class Epic(Spell):
    spellcraft_DC = models.IntegerField(validators=[MinValueValidator(0)])
    to_develop = models.TextField(max_length=1000, blank=True)
