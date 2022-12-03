import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.instance_of_song_1 = Song("Doo Wop", "Lauryn Hill")
        self.instance_of_song_2 = Song("Rise and Shine", "J Cole")
        self.instance_of_song_3 = Song("Murder She Wrote", "Chaka Demus & Pliers")
        self.instance_of_song_4 = Song("Testify", "Common")
        self.instance_of_song_5 = Song("Rise and Shine", "A Tribe Called Quest")
        self.instance_of_song_6 = Song("My All", "Mariah Carey")
        self.instance_of_song_7 = Song("Un-Break My Heart", "Toni Braxton")

    def test_song_has_artist(self):
        self.assertEqual("Un-Break My Heart", self.instance_of_song_7.artist)

    def test_song_has_song_title(self):
        self.assertEqual("Mariah Carey", self.instance_of_song_6.title)