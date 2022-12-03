import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.instance_of_guest1 = Guest("Jane", 65)
        self.instance_of_guest2 = Guest("Tammi", 24)
        self.instance_of_guest3 = Guest("Natalie", 33)
        self.instance_of_guest4 = Guest("Jayde", 32)
        self.instance_of_guest5 = Guest("Tess", 31)
        self.instance_of_guest6 = Guest("Chloe", 27)

    def test_guest_has_name(self):
        self.assertEqual("Jane", self.instance_of_guest1.name)

    def test_guest_has_age(self):
        self.assertEqual(65, self.instance_of_guest1.age)
