class Room():
    def __init__(self, room_number):
        self.room_number = room_number
        self.guest_list = []
        self.song_list = []

    def guest_count(self):
        return len(self.guest_list)

    def add_guest_to_list(self, guest):
        self.guest_list.append(guest)

    def remove_guest_from_list(self, guest):
        self.guest_list.remove(guest)

    def song_count(self):
        return len(self.song_list)

    def add_song_to_list(self, song):
        self.song_list.append(song)

    def remove_song_from_list(self, song):
        self.song_list.remove(song)

    # def print_song_list(self, list_of_songs):
