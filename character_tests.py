import unittest
from kreatorPostaci import Character, CharacterBuilder, CharacterCreator, HairColor, EyeColor, Armor, Weapon


class UnitTests(unittest.TestCase):
    def test_character_name(self):
        character = Character('John')
        self.assertEqual(character.name, 'John')

    def test_character_hair_color(self):
        character = Character('John')
        character.hair_color = HairColor.BLONDE
        self.assertEqual(character.hair_color, HairColor.BLONDE)

    def test_character_eye_color(self):
        character = Character('John')
        character.eye_color = EyeColor.BLUE
        self.assertEqual(character.eye_color, EyeColor.BLUE)

    def test_character_armor(self):
        character = Character('John')
        character.armor = Armor.PLATE
        self.assertEqual(character.armor, Armor.PLATE)

    def test_character_weapon(self):
        character = Character('John')
        character.weapon = Weapon.SWORD
        self.assertEqual(character.weapon, Weapon.SWORD)


class IntegrationTests(unittest.TestCase):
    def test_character_creation_and_representation(self):
        builder = CharacterBuilder()
        creator = CharacterCreator(builder)

        character = creator.create_character('John', HairColor.BLONDE, EyeColor.BLUE, Armor.PLATE, Weapon.SWORD)

        expected_output = "Character created:\nName: John\nHair Color: BLONDE\nEye Color: BLUE\nArmor: PLATE\nWeapon: SWORD"
        self.assertEqual(str(character), expected_output)


class AcceptanceTests(unittest.TestCase):
    def test_character_creation(self):
        builder = CharacterBuilder()
        creator = CharacterCreator(builder)

        character = creator.create_character('John', HairColor.BLONDE, EyeColor.BLUE, Armor.PLATE, Weapon.SWORD)

        self.assertIsInstance(character, Character)
        self.assertEqual(character.name, 'John')


if __name__ == '__main__':
    unittest.main()
