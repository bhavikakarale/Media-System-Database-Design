from SongDAO import SongDAO
import sys

class InformationProcessing:
    # def print_menu():
    #     print("Main Menu for Information Processing\n")
    #     print("Please select an option:\n")
    #     print("1. Get all Songs")
    #     print("2. Insert new Song")
    #     print("3. Update Song")
    #     print("4. Delete Song")
    #     # # print("5. Extras")
    #     print("\n0. Quit\n")

#     def process(self):
#         while True:
#             self.print_menu()
#             option = input()

#     if option == 1:
        
    def process(self):
        print("Welcome to Information Processing!")
        print("Main Menu for Information Processing\n")
        print("Please select an option:\n")
        print("1. Get all Songs")
        print("2. Insert new Song")
        print("3. Update Song")
        print("4. Delete Song")
        # # print("5. Extras")
        print("\n0. Quit\n")
        option = int(input())

        if option == 1:
            sd = SongDAO()
            sd.get_all_songs()
            # break
          
        #insert new song
        if option == 2:
            songMediaID = int(input("Enter media ID: "))
            songTrackNumber = int(input("Enter track number: "))
            songTitle = input("Enter title: ")
            songCountry = input("Enter country: ")
            songLanguage = input("Enter language: ")
            duration = input("Enter duration (hh:mm:ss): ")
            songRoyaltyRate = float(input("Enter royalty rate (e.g. 12.50): "))
            songAlbumID = int(input("Enter album ID: "))
            songreleaseDate = input("Enter Release Date (yyyy-mm-dd): ")
            sd = SongDAO()
            sd.insert_song_media(songMediaID)
            rowsInserted = sd.insert_song(songMediaID, duration, songTitle, songRoyaltyRate,songCountry,songLanguage, songAlbumID, songTrackNumber, songreleaseDate)
            if rowsInserted:
                print("New Song added successfully with Media ID " )
            else:
                print("Song not added") 
            sd.insert_song_media(songMediaID)
            sd.insert_song(songMediaID, duration, songTitle, songRoyaltyRate,songCountry,songLanguage, songAlbumID, songTrackNumber, songreleaseDate)
            sd.get_all_songs()
            # break
        


        if option == 3:
            updatesongmediaid = int(input("Enter media id of song to update: "))
            updatesongtitle = input("Enter new title: ")
            sd = SongDAO()
        #    rowsUpdated = sd.update_song(updatesongmediaid, updatesongtitle, updatesongcountry,updatesonglanguage, updatesongduration, updatesongreleaseDate, updatesongroyaltyrate,updatesongtracknumber)
            rowsUpdated = sd.update_song(updatesongtitle, updatesongmediaid)
            if rowsUpdated:
                print("Song updated successfully with Media ID " )
            else:
                print("Song not found") 
            sd.update_song(updatesongtitle, updatesongmediaid)
            sd.get_all_songs()
        
        if option == 4:
            deletesong = input("Enter Media ID to delete song: ")
            sd = SongDAO()
            rowsdeleted = sd.delete_song(deletesong)
            if rowsdeleted:
                print("Song deleted successfully with Media ID " )
            else:
                print("Song not found")
            sd.get_all_songs()

        if option == 0:
            print("Bye!")
            sys.exit(0)

if __name__ == "__main__":
    sd = SongDAO()
    sd.get_all_songs()
    sd.update_song()
    sd.delete_song()
    sd.insert_song_media()
    sd.insert_song()
