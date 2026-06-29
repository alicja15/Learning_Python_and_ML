class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
    
    def __len__(self):
        return len(self.songs)
    
    def __str__(self):
        return (f"Playlist {self.name} containing {len(self.songs)} songs")
         
my_playlist = Playlist("Radiohead: The Best Of")
my_playlist.add_song("No Surprises")
my_playlist.add_song("Creep")
my_playlist.add_song("All I Need")

print(len(my_playlist)) #3
print(my_playlist) #Playlist Radiohead: The Best Of containing 3 songs
    