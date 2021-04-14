import unittest
from production.batch import Batch

class TestBatch(unittest.TestCase):
    def test_batch_has_chocolate_name(self):
        batch = Batch(name = "Smi", kind = "løsvekt", boxes = 200)
        self.assertEqual(batch.name, "Smi")

    def test_batch_has_packaging_kind(self):
        batch = Batch(name = "Mint", kind = "single", boxes = 300)
        self.assertEqual(batch.kind, "single")

    def test_batch_has_boxes(self):
        batch = Batch("Schw", "single", 1234)
        self.assertEqual(batch.boxes, 1234)

    def test_batch_has_string_representation(self):
        batch = Batch("Krok", "single", 999)
        self.assertEqual(str(batch), "999 boxes of 'Krok' 'single'")

    def test_batch_has_technical_representation(self):
        batch = Batch("Milk", kind = "2pk", boxes = 400)
        self.assertEqual(repr(batch), "Batch(name = 'Milk', kind = '2pk', boxes = 400)")

    def test_batch_twopack_has_three_options(self):
        self.assertEqual(Batch._TWO_PACK, ("Dai", "Milk", "Smi"))

    def test_batch_løsvekt_has_two_options(self):
        self.assertEqual(Batch._LØSVEKT, ("Melk", "Smi"))

    def test_batch_single_has_nine_options(self):
        self.assertEqual(Batch._SINGLE, ("Dai", "Krok", "Melk", "Milk", "Mint", "Mjol", "Ore", "Smi", "Schw"))

    def test_batch_only_allows_for_valid_two_pack_options(self):
        with self.assertRaises(ValueError):
            Batch(name="Firk", kind="2pk", boxes=777)

    def test_batch_only_allows_for_valid_løsvekt_options(self):
        with self.assertRaises(ValueError):
            Batch(name="Mint", kind="løsvekt", boxes=555)

    def test_batch_only_allows_for_valid_single_options(self):
        with self.assertRaises(ValueError):
            Batch(name="Firklo", kind="single", boxes=500)

    def test_batch_boxes_per_hour_for_løsvekt(self):
        batch = Batch("Smi", "løsvekt", 200)
        self.assertEqual(batch.boxes_per_hour(), 60)

    def test_batch_boxes_per_hour_for_two_pack(self):
        batch = Batch("Milk", "2pk", 2000)
        self.assertEqual(batch.boxes_per_hour(), 180)

    def test_batch_boxes_per_hour_for_single(self):
        batch = Batch("Schw", "single", 1234)
        self.assertEqual(batch.boxes_per_hour(), 444)

    def test_batch_calculates_time_to_produce(self):
        batch = Batch("Smi", "løsvekt", 200)
        self.assertEqual(batch.calculate_time_to_produce(), (3, 20))

    def test_batch_displays_time_to_produce(self):
        batch = Batch("Smi", "løsvekt", 200)
        self.assertEqual(batch.display_time_to_produce(), "3 hours 20 min")
    
    def test_batch_displays_time_to_finish(self):
        batch = Batch("Smi", "løsvekt", 200)
        self.assertRegex(batch.display_time_to_finish(),
        "[0-9]{4}-[0-9]{1,2}-[0-9]{2}\s[0-9]+:[0-9]{2}:[0-9]{1,2}")