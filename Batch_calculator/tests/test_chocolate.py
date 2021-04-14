import unittest
from production.chocolate import Chocolate

class ChocolateTest(unittest.TestCase):
    def test_chocolate_has_name(self):
        chocolate = Chocolate(name = "Melk")
        self.assertEqual(chocolate.name, "Melk")
    def test_chocolate_has_string_representation(self):
        chocolate = Chocolate('Dai')
        self.assertEqual(str(chocolate), "Dai")
    def test_chocolate_has_technical_representation(self):
        chocolate = Chocolate('Krok')
        self.assertEqual(repr(chocolate), "Chocolate('Krok')")
    def test_chocolate_has_nine_brand_options(self):
        self.assertEqual(
            Chocolate.BRANDS,
            ("Dai", "Krok", "Melk", "Milk", "Mint", "Mjol", "Ore", "Smi", "Schw")
        )
    def test_chocolate_only_allows_for_valid_name(self):
        with self.assertRaises(ValueError):
            Chocolate(name = "Firklo")