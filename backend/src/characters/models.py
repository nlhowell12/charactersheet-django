from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from characters.character_choices import (
    ALIGNMENT_CHOICES, SEX_CHOICES, ZODIAC_CHOICES,
    DEFAULT_SKILLS)
from characters.class_choices import (
    HIT_DIE_CHOICES, SAVE_CHOICES
    )
from django.contrib.auth.models import User


class Character(models.Model):
    player = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='player')
    DM = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='DM')
    character_name = models.CharField(max_length=50)
    race = models.ForeignKey('Race', on_delete=models.SET_NULL, null=True)
    subrace = models.ForeignKey(
        'Subrace', on_delete=models.SET_NULL, null=True, blank=True)
    character_classes = models.ManyToManyField(
        'CharacterClass', related_name='character_class')
    hair_color = models.CharField(max_length=16, null=True, blank=True)
    eye_color = models.CharField(max_length=16, null=True, blank=True)
    height = models.CharField(
        max_length=6, null=True, blank=True,
        help_text='Height typically in feet')
    weight = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=False, blank=True, help_text='Weight in lbs', default=100)
    age = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=False, blank=True, default=25)
    max_hp = models.IntegerField(
        validators=[MinValueValidator(1)],
        null=False, blank=False, default=1)
    current_hp = models.IntegerField(
        null=False, blank=False, default=1)
    base_strength = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    base_dexterity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    base_constitution = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    base_intelligence = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    base_wisdom = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    base_charisma = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False, blank=False, default=10)
    personal_traits = models.TextField(null=False, blank=True, default='')
    ideals = models.TextField(null=False, blank=True, default='')
    flaws = models.TextField(null=False, blank=True, default='')
    notes = models.TextField(null=False, blank=True, default='')
    sex = models.CharField(
        max_length=10,
        choices=SEX_CHOICES, default='Male', null=False, blank=False)
    alignment = models.CharField(
        choices=ALIGNMENT_CHOICES, default='LG', null=False, blank=False,
        max_length=2)
    zodiac_sign = models.CharField(
        choices=ZODIAC_CHOICES, default=0, null=False, blank=False,
        max_length=20)
    skills = models.CharField(
        max_length=1000, default=DEFAULT_SKILLS)
    feats = models.ManyToManyField(
        'Feat', related_name='+', blank=True)
    img = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.character_name}'


class Race(models.Model):
    racial_name = models.CharField(max_length=15)
    classification = models.CharField(max_length=100, default='Humanoid')
    attribute_bonuses = models.CharField(max_length=100, blank=True, null=True)
    skill_bonuses = models.CharField(max_length=100, blank=True, null=True)
    feats = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=25, default='Medium')
    speed = models.CharField(max_length=10, default='30 ft')
    favored_class = models.CharField(max_length=50, default='Any')
    automatic_languages = models.CharField(max_length=100, blank=True)
    bonus_languages = models.CharField(max_length=100, blank=True)
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
    attribute_bonuses = models.CharField(max_length=100, blank=True, null=True)
    skill_bonuses = models.CharField(max_length=100, blank=True, null=True)
    feats = models.CharField(max_length=100, blank=True, null=True)
    favored_class = models.CharField(max_length=50, default='Any')
    automatic_languages = models.CharField(max_length=200, blank=True)
    bonus_languages = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    special_abilities = models.TextField()

    def __str__(self):
        return self.subrace_name


class BaseClass(models.Model):
    class Meta:
        verbose_name_plural = 'Classes'

    class_name = models.CharField(max_length=20)
    hit_die = models.IntegerField(choices=HIT_DIE_CHOICES, default=4)
    base_attack_bonus = models.CharField(
        max_length=1000,
        choices=[('Poor', 'Poor'), ('Moderate', 'Moderate'), ('Good', 'Good')],
        default='Poor')
    class_skills = models.CharField(
        max_length=1000, blank=True)
    skill_points = models.IntegerField(
        validators=[MinValueValidator(2)], default=2)
    class_abilities = models.CharField(
        max_length=1000, blank=True)
    fort = models.CharField(
        max_length=4, choices=SAVE_CHOICES, default='Poor'
        )
    reflex = models.CharField(
        max_length=4, choices=SAVE_CHOICES, default='Poor'
        )
    will = models.CharField(
        max_length=4, choices=SAVE_CHOICES, default='Poor'
        )
    spells_per_level = models.CharField(
        max_length=1500, null=True, blank=True)
    spells_known = models.IntegerField(
        validators=[MinValueValidator(0)],
        null=True,
        blank=True
    )

    def __str__(self):
        return self.class_name


class CharacterClass(models.Model):
    class Meta:
        verbose_name_plural = 'Character Classes'

    base_class = models.ForeignKey(
        BaseClass, on_delete=models.CASCADE, null=True)
    level = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.base_class} {self.level}'


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
        return f'{self.feat_classification} - {self.feat_name}'
