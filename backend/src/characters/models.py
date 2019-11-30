from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from characters.character_choices import (
    ALIGNMENT_CHOICES, SEX_CHOICES, ZODIAC_CHOICES, ATTRIBUTE_CHOICES)
from characters.class_choices import (HIT_DIE_CHOICES)
from characters.equipment_choices import (SPELL_FAILURE_CHANCES)
from characters.bonuses import (BONUS_TYPES)


class Character(models.Model):
    character_Name = models.CharField(max_length=50)
    race = models.ForeignKey('Race', on_delete=models.SET_NULL, null=True)
    character_classes = models.ManyToManyField(
        'CharacterClass', related_name='character')
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
    alignment = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(9)],
        choices=ALIGNMENT_CHOICES, default=0, null=False, blank=False)
    zodiac_Sign = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(11)],
        choices=ZODIAC_CHOICES, default=0, null=True, blank=True)
    skills = models.ManyToManyField(
        'CharacterSkill', related_name='+', blank=True)
    feats = models.ManyToManyField(
        'Feat', related_name='+', blank=True)

    def __str__(self):
        return self.character_Name


class Race(models.Model):
    racial_name = models.CharField(max_length=15)
    attribute_bonuses = models.ManyToManyField(
      'AttributeBonus', related_name='+')
    skill_bonuses = models.ManyToManyField(
      'SkillBonus', related_name='+')
    description = models.TextField()
    special_abilities = models.TextField()
    non_playable = models.BooleanField(default=False)

    def __str__(self):
        return self.racial_name


class Subrace(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    subrace_name = models.CharField(max_length=15)
    attribute_bonus = models.ManyToManyField(
      'AttributeBonus', related_name='+')
    skill_bonuses = models.ManyToManyField(
       'SkillBonus', related_name='+')
    description = models.TextField()
    special_abilities = models.TextField()

    def __str__(self):
        return self.subrace_name


class BaseClass(models.Model):
    class_name = models.CharField(max_length=20)
    hit_die = models.IntegerField(choices=HIT_DIE_CHOICES, default=4)
    class_skills = models.ManyToManyField('Skill', related_name='+')

    def __str__(self):
        return self.class_name


class CharacterClass(BaseClass):
    level = models.IntegerField(validators=[MinValueValidator(0)], default=0)


class Skill(models.Model):
    skill_name = models.CharField(max_length=50)
    synergies = models.ManyToManyField('self', related_name='+', blank=True)
    description = models.TextField(max_length=1500)

    def __str__(self):
        return self.skill_name


class CharacterSkill(Skill):
    rank = models.IntegerField(validators=[MinValueValidator(0)])


class Feat(models.Model):
    feat_name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    skill_bonuses = models.ManyToManyField(
        'SkillBonus', related_name='+')
    attribute_bonuses = models.ManyToManyField(
        'AttributeBonus', related_name='+')

    def __str__(self):
        return self.feat_name


class Equipment(models.Model):
    item_name = models.CharField(max_length=50)
    weight = models.IntegerField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.item_name


class Weapon(Equipment):
    damage_dice = models.CharField(max_length=5)
    two_handed = models.BooleanField(default=False)
    crit_range = models.CharField(max_length=10, default='20/x2')
    range_increment = models.IntegerField(validators=[MinValueValidator(0)])


class Armor(Equipment):
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


class AttributeBonus(models.Model):
    attribute = models.CharField(
        choices=ATTRIBUTE_CHOICES, default='strength',
        null=False, blank=False, max_length=20)
    bonus = models.IntegerField()
    bonus_type = models.CharField(
        choices=BONUS_TYPES, default='untyped', max_length=10)

    def __str__(self):
        return '{type}: {attribute} +{bonus}'.format(
            type=self.bonus_type, attribute=self.attribute,
            bonus=self.bonus)


class SkillBonus(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    bonus = models.IntegerField()
    bonus_type = models.CharField(
        choices=BONUS_TYPES, default='untyped', max_length=10)

    def __str__(self):
        return '{type}: {skill} +{bonus}'.format(
            type=self.bonus_type, skill=self.skill.skill_name,
            bonus=self.bonus)
