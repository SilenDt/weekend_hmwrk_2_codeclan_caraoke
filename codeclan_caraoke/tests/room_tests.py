import unittest
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.instance_of_room = Room([], [])

    # def test_add_guest_to_list(self):