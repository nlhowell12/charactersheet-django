from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from characters.character_choices import (
    ALIGNMENT_CHOICES, SEX_CHOICES, ZODIAC_CHOICES)
from characters.class_choices import (
    HIT_DIE_CHOICES, SAVE_CHOICES
    )
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
    class_skills = models.ManyToManyField(
        'Skill', related_name='+', blank=True)
    skill_points = models.IntegerField(
        validators=[MinValueValidator(2)], default=2)
    class_abilities = models.ManyToManyField(
        'ClassAbility', blank=True)
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
    class Meta:
        ordering = ['feat_classification', 'feat_name']
    feat_name = models.CharField(max_length=50)
    feat_classification = models.CharField(max_length=50, blank=True)
    benefit = models.TextField(max_length=1000)
    prerequisites = models.TextField(max_length=1000)
    attribute_bonuses = models.CharField(max_length=50, blank=True, null=True)
    skill_bonuses = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.feat_classification, self.feat_name)
