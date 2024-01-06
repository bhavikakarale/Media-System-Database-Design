from SongDAO import SongDAO
from ArtistDAO import ArtistDAO 
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
        print("5. Get all Artists")
        print("6. Insert new Artist")
        print("7. Delete Artist")
        print("8. Update Artist Details")
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

        if option == 5:
            ad = ArtistDAO()
            ad.get_all_artists()

        if option == 6:
            ArtistID = int(input("Insert New Artist ID: "))
            Name = input("Insert New Artist Name: ")
            Status = input("Insert New Artist Status: ")
            Type = input("Insert New Artist Type: ")
            Country = input("Insert New Artist Country: ")
            PrimaryGenre = input("Insert New Artist Primary Genre: ")
            ad = ArtistDAO()
            Artistinserted = ad.insert_artist(ArtistID, Name, Status, Type, Country, PrimaryGenre)
            if Artistinserted:
                print("Artist Details inserted successfully")

        if option == 7:
            deleteArtistID = input("Enter Artist ID to delete: ")
            ad = ArtistDAO()
            artistdeleted = ad.delete_artist(deleteArtistID)
            if artistdeleted:
                print("Artist deleted successfully!")
            else:
                print("Artist not found")

        if option == 8:
            artistName = input("Insert new Artist name to update: ")
            ad = ArtistDAO()
            artistupdated = ad.update_artist(artistName)
            if artistupdated:
                print("Artist Updated Successfully")
            else:
                print("Could not update the Artist Details")

        

        if option == 0:
            print("Bye!")
            sys.exit(0)

if __name__ == "__main__":
    sd = SongDAO()
    ad = ArtistDAO()
    sd.get_all_songs()
    sd.update_song()
    sd.delete_song()
    sd.insert_song_media()
    sd.insert_song()
    ad.get_all_artists()
    
