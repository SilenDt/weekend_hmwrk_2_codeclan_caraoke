import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.instance_of_guest1 = Guest("Jane")
        self.instance_of_guest2 = Guest("Tammi")
        self.instance_of_guest3 = Guest("Natalie")
        self.instance_of_guest4 = Guest("Jayde")
        self.instance_of_guest5 = Guest("Tess")
        self.instance_of_guest6 = Guest("Chloe")

    def test_guest_has_name(self):
        self.assertEqual("Jane", self.instance_of_guest1.name)

    