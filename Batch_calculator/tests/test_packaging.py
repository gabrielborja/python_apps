import unittest
from production.packaging import Packaging

class PackagingTest(unittest.TestCase):
    def test_packaging_has_name(self):
        packaging = Packaging(kind = "single")
        self.assertEqual(packaging.kind, "single")
    def test_packaging_has_string_representation(self):
        packaging = Packaging(kind = "2pk")
        self.assertEqual(str(packaging), "2pk")
    def test_packaging_has_technical_representation(self):
        packaging = Packaging(kind = "løsvekt")
        self.assertEqual(repr(packaging), "Packaging('løsvekt')")
    def test_packaging_has_three_kind_options(self):
        self.assertEqual(
            Packaging.KINDS, ("single", "2pk", "løsvekt"))
    def test_packaging_only_allows_for_valid_kind(self):
        with self.assertRaises(ValueError):
            Packaging(kind = "Multi-pack") 