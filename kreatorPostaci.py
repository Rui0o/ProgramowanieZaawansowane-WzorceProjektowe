from enum import Enum
import time

class HairColor(Enum):
    BLONDE = 'BLONDE'
    BROWN = 'BROWN'
    BLACK = 'BLACK'
    RED = 'RED'

class EyeColor(Enum):
    BLUE = 'BLUE'
    GREEN = 'GREEN'
    BROWN = 'BROWN'
    HAZEL = 'HAZEL'

class Armor(Enum):
    PLATE = 'PLATE'
    LEATHER = 'LEATHER'
    CLOTH = 'CLOTH'

class Weapon(Enum):
    SWORD = 'SWORD'
    AXE = 'AXE'
    BOW = 'BOW'

class Character:
    def __init__(self, name):
        self.name = name
        self.hair_color = None
        self.eye_color = None
        self.armor = None
        self.weapon = None

    def __str__(self):
        return f"Character created:\nName: {self.name}\nHair Color: {self.hair_color.value}\nEye Color: {self.eye_color.value}\nArmor: {self.armor.value}\nWeapon: {self.weapon.value}"

class CharacterBuilder:
    def __init__(self):
        self.character = Character('')

    def set_name(self, name):
        self.character.name = name

    def set_hair_color(self, hair_color):
        self.character.hair_color = hair_color

    def set_eye_color(self, eye_color):
        self.character.eye_color = eye_color

    def set_armor(self, armor):
        self.character.armor = armor

    def set_weapon(self, weapon):
        self.character.weapon = weapon

class CharacterCreator:
    def __init__(self, builder):
        self.builder = builder

    def create_character(self, name, hair_color, eye_color, armor, weapon):
        self.builder.set_name(name)
        self.builder.set_hair_color(hair_color)
        self.builder.set_eye_color(eye_color)
        self.builder.set_armor(armor)
        self.builder.set_weapon(weapon)
        return self.builder.character


def main():
    builder = CharacterBuilder()
    creator = CharacterCreator(builder)

    character1 = creator.create_character('John', HairColor.BLONDE, EyeColor.BLUE, Armor.PLATE, Weapon.SWORD)
    print(character1)
    print("-----")

    character2 = creator.create_character('Emily', HairColor.RED, EyeColor.GREEN, Armor.LEATHER, Weapon.BOW)
    print(character2)
    print("-----")

    character3 = creator.create_character('Michael', HairColor.BROWN, EyeColor.BROWN, Armor.CLOTH, Weapon.AXE)
    print(character3)

if __name__ == '__main__':
    main()
