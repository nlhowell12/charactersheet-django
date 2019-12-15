from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from characters.character_choices import (
    ALIGNMENT_CHOICES, SEX_CHOICES, ZODIAC_CHOICES)
from characters.class_choices import (
    HIT_DIE_CHOICES, SAVE_CHOICES
    )
from characters.equipment_choices import (
    SPELL_FAILURE_CHANCES, BODY_SLOT_CHOICES
    )
from characters.bonuses import (BONUS_TYPES)
from django.contrib.auth.models import User


class Character(models.Model):
    player = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='player')
    DM = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='DM')
    character_Name = models.CharField(max_length=50)
    race = models.ForeignKey('Race', on_delete=models.SET_NULL, null=True)
    character_Classes = models.ManyToManyField(
        'CharacterClass', related_name='character_class')
    hair_Color = models.CharField(max_length=16, null=True, blank=True)
    eye_Color = models.CharField(max_length=16, null=True, blank=True)
    height = models.CharField(
        max_length=6, null=True, blank=True,
        help_text='Height typically in feet')
    weight = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=False, blank=True, help_text='Weight in lbs', default=100)
    age = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=False, blank=True, default=25)
    max_HP = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=False, blank=False, default=1)
    current_HP = models.IntegerField(
        null=False, blank=False, default=1)
    base_Strength = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    base_Dexterity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    base_Constitution = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    base_Intelligence = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    base_Wisdom = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    base_Charisma = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    personal_Traits = models.TextField(null=False, blank=True, default='')
    ideals = models.TextField(null=False, blank=True, default='')
    flaws = models.TextField(null=False, blank=True, default='')
    notes = models.TextField(null=False, blank=True, default='')
    sex = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(3)],
        choices=SEX_CHOICES, default=0, null=False, blank=False)
    alignment = models.CharField(
        choices=ALIGNMENT_CHOICES, default='LG', null=False, blank=False,
        max_length=2)
    zodiac_Sign = models.CharField(
        choices=ZODIAC_CHOICES, default=0, null=False, blank=False,
        max_length=20)
    skills = models.ManyToManyField(
        'CharacterSkill', related_name='+', blank=True)
    feats = models.ManyToManyField(
        'Feat', related_name='+', blank=True)

    def __str__(self):
        return self.character_Name


class Race(models.Model):
    racial_name = models.CharField(max_length=15)
    attribute_bonuses = models.CharField(max_length=50, blank=True, null=True)
    skill_bonuses = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    special_abilities = models.TextField()
    playable = models.BooleanField(default=True)

    def __str__(self):
        return self.racial_name


class Subrace(models.Model):
    class Meta:
        verbose_name_plural = 'Sub-Races'

    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    subrace_name = models.CharField(max_length=30)
    attribute_bonuses = models.CharField(max_length=50, blank=True, null=True)
    skill_bonuses = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    special_abilities = models.TextField()

    def __str__(self):
        return self.subrace_name


class BaseClass(models.Model):
    class Meta:
        verbose_name_plural = 'Classes'

    class_name = models.CharField(max_length=20)
    hit_die = models.IntegerField(choices=HIT_DIE_CHOICES, default=4)
    class_skills = models.ManyToManyField('Skill', related_name='+')
    skill_points = models.IntegerField(
        validators=[MinValueValidator(2)], default=2)
    class_abilities = models.ManyToManyField(
        'ClassAbility')
    fort = models.CharField(
        max_length=4, choices=SAVE_CHOICES, default='Poor'
        )
    reflex = models.CharField(
        max_length=4, choices=SAVE_CHOICES, default='Poor'
        )
    will = models.CharField(
        max_length=4, choices=SAVE_CHOICES, default='Poor'
        )

    def __str__(self):
        return self.class_name


class ClassAbility(models.Model):
    class Meta:
        verbose_name_plural = 'Class Abilities'

    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class CharacterClass(models.Model):
    class Meta:
        verbose_name_plural = 'Character Classes'

    base_class = models.ForeignKey(
        BaseClass, on_delete=models.CASCADE, null=True)
    level = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return '{} {}'.format(self.base_class.class_name, self.level)


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    synergies = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=1500)

    def __str__(self):
        return self.skill_name


class CharacterSkill(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    rank = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.skill.skill_name


class Feat(models.Model):
    feat_name = models.CharField(max_length=50)
    benefit = models.TextField(max_length=1000)
    prerequisites = models.TextField(max_length=1000)
    attribute_bonuses = models.CharField(max_length=50, blank=True, null=True)
    skill_bonuses = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.feat_name


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


class Spell(models.Model):
    class Meta:
        ordering = ['level', 'name']

    name = models.CharField(max_length=50)
    level = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)])
    class_spell_list = models.ForeignKey(BaseClass, on_delete=models.CASCADE)
    descriptors = models.CharField(max_length=50)
    casting_time = models.CharField(max_length=50)
    spell_range = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    save = models.CharField(max_length=50, null=True, blank=True)
    bonus_tyoe = models.CharField(max_length=50)
    damage_type = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return '{} - {}'.format(self.level, self.name)


class Song(Spell):
    chord = models.CharField(max_length=20)


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


class PactInvocation(models.Model):
    pact = models.CharField(max_length=100)


class Mystery(models.Model):
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
