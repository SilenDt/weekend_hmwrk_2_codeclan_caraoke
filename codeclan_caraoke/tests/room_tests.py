import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
    
        self.instance_of_room = Room(10)  
        self.guest = "Jane"
        self.instance_of_song_1 = Song("Ubreak My Heart", "Toni Braxton")
        self.instance_of_song_2 = Song("Rise and Shine", "J Cole")
        self.instance_of_song_3 = Song("Murder She Wrote", "Chaka Demus & Pliers")
        self.instance_of_song_4 = Song("Testify", "Common")
        self.instance_of_song_5 = Song("Rise and Shine", "A Tribe Called Quest")
        self.instance_of_song_6 = Song("My All", "Mariah Carey")
        self.instance_of_song_7 = Song("Doo Wop", "Lauryn Hill")

    def test_room_has_room_number(self):
        self.assertEqual(10, self.instance_of_room.room_number)

    def test_guest_list_starts_empty(self):
        self.assertEqual(0, self.instance_of_room.guest_count())

    def test_can_add_guest_to_guest_list(self):
        self.instance_of_room.add_guest_to_list(self.guest)
        self.assertEqual(1, self.instance_of_room.guest_count())

    def test_can_remove_guest_from_list(self):
        self.instance_of_room.add_guest_to_list(self.guest)
        self.instance_of_room.remove_guest_from_list(self.guest)
        self.assertEqual(0, self.instance_of_room.guest_count())

    def test_song_list_starts_empty(self):
        self.assertEqual(0, self.instance_of_room.song_count())

    def test_can_add_song_to_song_list(self):
        self.instance_of_room.add_song_to_list(self.instance_of_song_1)
        self.assertEqual(1, self.instance_of_room.song_count())

    def test_can_remove_song_from_list(self):
        self.instance_of_room.add_song_to_list(self.instance_of_song_1)
        self.instance_of_room.remove_song_from_list(self.instance_of_song_1)
        self.assertEqual(0, self.instance_of_room.song_count())

    # def test_print_song_list(self):
        