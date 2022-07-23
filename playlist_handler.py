
# Declare class that contains queue with playlist
class Playlist_Queue:

    # Declare class the contains songs information
    class Song:
        def __init__(self, song_name, artist, duration):
            self.song_name = song_name
            self.artist = artist
            self.duration = duration

        # Method to be able to use the print function with the dequeued song
        def __str__(self):
            
            return "The song '" + self.song_name + "' by " + self.artist + " is being played - Duration: " + self.duration + " minutes" 
    
    # Method create the queue for the playlist with a list
    def __init__(self):
        self.songs_playlist = []
        self.max_size = 20          #Declare the size of the queue

    # Method to insert songs to the playlist
    def enqueue(self):
        # Prompt for song's information
        if len(self.songs_playlist) <= self.max_size:
            song_name = input("Enter the name of the song: ")
            song_name_format = song_name.capitalize()               # Capitalize song's name to match input by user
            artist = input("Enter the name of the artist: ")
            artist_format = artist.capitalize()                     # Capitalize artist's name to match input by user
            duration = input("Enter song duration in minutes: ")
            new_song = Playlist_Queue.Song(song_name_format, artist_format, duration)
            self.songs_playlist.append(new_song)                    # Enqueue a new song in the playlist
        else:
            print("\nQueue is full. No more songs can be added.")
    
    # Method to remove the song from the front of the queue
    def dequeue(self):    
        return self.songs_playlist.pop(0)
    
    # Method that return the length of the queue
    def len(self):
        return len(self.songs_playlist)
    
    # Method that returns the waiting time until a specific song is played
    def wait_to_play(self, selected_song):
        time = 0
        # Loop through the playlist to calculate the waiting time
        for song in self.songs_playlist:
            if  selected_song != song.song_name:
                sum_time = float(song.duration)
                time += sum_time
            if  selected_song == song.song_name:
                return time

# Create a queue for the playlist
play_list = Playlist_Queue()

request = 1
exit_menu = "no"

# Create menu for user
while exit_menu == "no":
    print("Playlist Menu: ")
    print("1) Add songs to the playlist")
    print("2) Play playlist")
    print("3) Calculate how much time it's going to take until a specific song is played")
    print("4) Exit")
    operation = int(input("\nSelect operation: "))

    # Add to the playlist
    if operation == 1:
        while request == 1:
            
            play_list.enqueue()
            request = int(input("\nDo you want to add another song? (Enter 1 for yes and 0 for no): "))
            print()

    # Play songs from playlist
    elif operation == 2:
        print()
        # Dequeue songs from playlist as long as the queue is not empty
        while play_list.len() != 0:
            served_song = play_list.dequeue()

            print(served_song)
    
    # Return the waiting time until a specific song is played
    elif operation == 3:
        song_name = input("Do you want to know how much time it's going to take until it plays an specific song? Please enter the name of the song: ").capitalize()
        waiting_time = play_list.wait_to_play(song_name)
        print(f"\nYou will need to wait for {waiting_time} minutes until you can listen '{song_name}'")
    
    # Exit the menu
    elif operation == 4:
        exit_menu = "yes"
    
    print()