ALIGNMENT_CHOICES = (
    ('LG', 'Lawful Good'),
    ('NG', 'Neutral Good'),
    ('CG', 'Chaotic Good'),
    ('LN', 'Lawful Neutral'),
    ('N', 'True Neutral'),
    ('CN', 'Chaotic Neutral'),
    ('LE', 'Lawful Evil'),
    ('NE', 'Neutral Evil'),
    ('CE', 'Chaotic Evil'),
)

SEX_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

ZODIAC_CHOICES = (
    ('Aries', 'Aries'),
    ('Leo', 'Leo'),
    ('Cancer', 'Cancer'),
    ('Pisces', 'Pisces'),
    ('Scorpio', 'Scorpio'),
    ('Taurus', 'Taurus'),
    ('Sagittarius', 'Sagittarius'),
    ('Gemini', 'Gemini'),
    ('Virgo', 'Virgo'),
    ('Libra', 'Libra'),
    ('Caricorn', 'Capricorn'),
    ('Aquarius', 'Aquarius'),
)

ATTRIBUTE_CHOICES = (
    ('strength', 'Strength'),
    ('dexterity', 'Dexterity'),
    ('constitution', 'Constituion'),
    ('intelligence', 'Intelligence'),
    ('wisdom', 'Wisdom'),
    ('charisma', 'Charisma')
)

DEFAULT_SKILLS = {
    'Acrobatics': {
        'ranks': 0, 'attribute': 'Dexterity',
        'trained': True, 'armor_check': True},
    'Artifice': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Autohypnosis': {
        'ranks': 0, 'attribute': 'Wisdom',
        'trained': True, 'armor_check': False},
    'Bluff': {
        'ranks': 0, 'attribute': 'Charisma',
        'trained': False, 'armor_check': False},
    'Climb': {
        'ranks': 0, 'attribute': 'Strength',
        'trained': False, 'armor_check': True},
    'Concentration': {
        'ranks': 0, 'attribute': 'Constitution',
        'trained': False, 'armor_check': False},
    'Craft': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': False, 'armor_check': False},
    'Decipher Script': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Diplomacy': {
        'ranks': 0, 'attribute': 'Charisma',
        'trained': False, 'armor_check': False},
    'Disguise': {
        'ranks': 0, 'attribute': 'Charisma',
        'trained': False, 'armor_check': False},
    'Escape Artist': {
        'ranks': 0, 'attribute': 'Dexterity',
        'trained': False, 'armor_check': True},
    'Forgery': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': False, 'armor_check': False},
    'Handle Animal': {
        'ranks': 0, 'attribute': 'Wisdom',
        'trained': True, 'armor_check': False},
    'Heal': {
        'ranks': 0, 'attribute': 'Wisdom',
        'trained': False, 'armor_check': False},
    'Intimidate': {
        'ranks': 0, 'attribute': 'Charisma',
        'trained': False, 'armor_check': False},
    'Knowledge: Arcana': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Knowledge: Architecture and Engineering': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Knowledge: Dungeoneering': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Knowledge: History': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Knowledge: Local': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Knowledge: Military and Tactics': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Knowledge: Nature': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Knowledge: Nobility and Royalty': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Knowledge: Psionics': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Knowledge: Religion': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Knowledge: The Planes': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Magecraft': {
        'ranks': 0, 'attribute': 'Intelligence',
        'trained': True, 'armor_check': False},
    'Perception': {
        'ranks': 0, 'attribute': 'Wisdom',
        'trained': False, 'armor_check': False},
    'Perform': {
        'ranks': 0, 'attribute': 'Charisma',
        'trained': False, 'armor_check': False},
    'Ride': {
        'ranks': 0, 'attribute': 'Dexterity',
        'trained': False, 'armor_check': False},
    'Sense Motive': {
        'ranks': 0, 'attribute': 'Wisdom',
        'trained': False, 'armor_check': False},
    'Sleight of Hand': {
        'ranks': 0, 'attribute': 'Dexterity',
        'trained': True, 'armor_check': True},
    'Speak Language': {'ranks': 0, 'languages': []},
    'Stealth': {
        'ranks': 0, 'attribute': 'Dexterity',
        'trained': False, 'armor_check': True},
    'Survival': {
        'ranks': 0, 'attribute': 'Wisdom',
        'trained': False, 'armor_check': False},
    'Swim': {
        'ranks': 0, 'attribute': 'Strength',
        'trained': False, 'armor_check': True},
    'Use Rope': {
        'ranks': 0, 'attribute': 'Dexterity',
        'trained': False, 'armor_check': False},
}
