from characters.models import (
    Feat, Character, CharacterClass,
    Race, BaseClass, Subrace
    )
from django.contrib.auth.models import User
from rest_framework.response import Response
from xlrd import open_workbook


def generate_feats(feat_file):
    delete_feats()
    book = open_workbook(file_contents=feat_file.read())
    sheet = book.sheets()[0]
    rows = sheet.get_rows()
    for row in rows:
        if(row[0].ctype == 1):
            Feat.objects.create(
                feat_classification=row[0].value,
                feat_name=row[1].value,
                prerequisites=row[2].value,
                benefit=row[3].value
            )
    return Response({'Upload Succesful'})


def delete_feats():
    return Feat.objects.all().delete()


def serve_feats():
    feats = Feat.objects.all()
    parsed_feats = {}
    for feat in feats:
        parsed_feat = {
            'feat_name': feat.feat_name,
            'prerequisites': feat.prerequisites,
            'benefit': feat.benefit
        }
        if feat.feat_classification in parsed_feats:
            parsed_feats[feat.feat_classification] = [
                *parsed_feats[feat.feat_classification], parsed_feat]
        else:
            parsed_feats[feat.feat_classification] = [parsed_feat]
    return parsed_feats


def parse_feat(feat):
    return {
        'feat_classification': feat.feat_classification,
        'feat_name': feat.feat_name,
        'prerequisites': feat.prerequisites,
        'benefit': feat.benefit
        }


def set_character_classes(character, character_classes):
    for character_class in character_classes:
        new_class = CharacterClass.objects.create(
            base_class=BaseClass.objects.filter(
                class_name=character_class['class_name']).first(),
            level=character_class['level']
        )
        character.character_classes.add(new_class)


def set_character_feats(character, character_feats):
    for feat in character_feats:
        new_feat = Feat.objects.filter(feat_name=feat).first()
        character.feats.add(new_feat)


def add_new_character(character):
    if not Character.objects.filter(character_name=character['character_name']).first():
        new_character = Character.objects.create(
            player=User.objects.filter(username=character['player']).first(),
            DM=User.objects.filter(username=character['DM']).first(),
            character_name=character['character_name'],
            race=Race.objects.filter(
                racial_name=character['race']).first(),
            subrace=Subrace.objects.filter(
                subrace_name=character['subrace']).first(),
            hair_color=character['hair_color'],
            eye_color=character['eye_color'],
            height=character['height'],
            weight=character['weight'],
            age=character['age'],
            max_hp=character['max_hp'],
            current_hp=character['current_hp'],
            base_strength=character['base_strength'],
            base_dexterity=character['base_dexterity'],
            base_constitution=character['base_constitution'],
            base_intelligence=character['base_intelligence'],
            base_wisdom=character['base_wisdom'],
            base_charisma=character['base_charisma'],
            personal_traits=character['personal_traits'],
            ideals=character['ideals'],
            flaws=character['flaws'],
            notes=character['notes'],
            sex=character['sex'],
            alignment=character['alignment'],
            zodiac_sign=character['zodiac_sign'],
            skills=character['skills'],
        )
        set_character_classes(new_character, character['character_classes'])
        set_character_feats(new_character, character['feats'])
        return {'message': 'Character added successfully', 'status': True}
    else:
        return {'message': 'Character already exists', 'status': False}