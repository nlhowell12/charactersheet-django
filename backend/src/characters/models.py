from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Character(models.Model):
    character_Name = models.CharField(max_length=50)
    hair_Color = models.CharField(max_length=16, null=True, blank=True)
    eye_Color = models.CharField(max_length=16, null=True, blank=True)
    height = models.CharField(max_length=6, null=True,
                              blank=True, help_text='height typically in feet')
    weight = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], null=True, blank=True)
    age = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], null=True, blank=True)
    max_HP = models.IntegerField(validators=[MinValueValidator(
        1), MaxValueValidator(1000)], null=True, blank=True)
    base_Strength = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], null=True, blank=True)
    base_Dexterity = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], null=True, blank=True)
    base_Constitution = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], null=True, blank=True)
    base_Intelligence = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], null=True, blank=True)
    base_Wisdom = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], null=True, blank=True)
    base_Charisma = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(1000)], null=True, blank=True)
    personal_Traits = models.TextField(null=True, blank=True)
    ideals = models.TextField(null=True, blank=True)
    flaws = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    sex = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(
        2)], null=True, blank=True, help_text='change to fk or manage in frontend')
    alignment = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(
        7)], null=True, blank=True, help_text='change to fk or manage in frontend')
    zodiac_Sign = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(
        11)], null=True, blank=True, help_text='change to fk or manage in frontend')

    def __str__(self):
        return self.character_Name
