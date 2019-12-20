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
    chord = models.CharField(max_length=20)


class Arcane(Spell):
    school = models.CharField(max_length=20)


class Prayer(Spell):
    domain = models.CharField(max_length=20)


class Chant(Spell):
    sphere = models.CharField(max_length=20)


class Power(Spell):
    discipline = models.CharField(max_length=20)


class DisciplinePower(Power):
    discipline_list = models.CharField(max_length=15)


class Vestige(models.Model):
    class Meta:
        ordering = ['name']

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
        ordering = ['level', 'name']

    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    level = models.IntegerField(validators=[MinValueValidator(1)])
    maneuver_type = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return '{} - {}'.format(self.level, self.name)


class Invocation(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    level_equivalent = models.CharField(max_length=100, null=True, blank=True)
    invocation_type = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=100, null=True, blank=True)
    save = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return '{} - {}'.format(self.pact, self.grade)


class PactInvocation(Invocation):
    pact = models.CharField(max_length=100)


class Mystery(models.Model):
    class Meta:
        verbose_name_plural = 'Mysteries'

    name = models.CharField(max_length=50)
    mystery_rank = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    path_level = models.IntegerField()
    mystery_range = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    save = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return '{} - {}. {}'.format(
            self.mystery_rank, self.path_level, self.name)


class Epic(Spell):
    spellcraft_DC = models.IntegerField(validators=[MinValueValidator(0)])
    to_develop = models.TextField(max_length=1000, blank=True)
